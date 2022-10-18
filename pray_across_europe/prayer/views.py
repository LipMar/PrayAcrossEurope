from django.shortcuts import render
from .models import Prayer
from datetime import datetime

# Create your views here.
def get_matched_prayer(current_date): #to jest zwykła funkcja

    found_prayer = Prayer.objects.all().filter(date1__day=current_date.day, date1__month=current_date.month) | \
                   Prayer.objects.all().filter(date2__day=current_date.day, date2__month=current_date.month) | \
                   Prayer.objects.all().filter(date3__day=current_date.day, date3__month=current_date.month) | \
                   Prayer.objects.all().filter(date4__day=current_date.day, date4__month=current_date.month)

    return found_prayer #ta wartosc jest wykorzystywana w widoku poniżej

def calculate_year(current_date): #to jest również zwykła funkcja
    current_month = current_date.month  # zwraca wartosc od 1 do 12
    if current_month <= 5:
        year = current_date.year
    else:
        year = current_date.year + 1
    return year

def prayer(request): #a to jest widok bo (request)
    #current_date = datetime(2023,5,12)
    current_date = datetime.now()
    found_prayer = get_matched_prayer(current_date)

    if len(found_prayer) == 0:
        year = calculate_year(current_date)
        TARGET_DATE = datetime.strptime(f"13-05-{year}","%d-%m-%Y")

        remaining_days = (TARGET_DATE - current_date).days
        return render(request, 'prayer/counter.html', {'remaining_days': remaining_days})

    return render(request, 'prayer/prayer.html', {'prayer': found_prayer.first(), 'today_date': current_date.strftime("%d-%m-%y")}) #musi być found_prayer.first() bo inaczej zwraca quesry set, a nie pojedynczy obiekt (nawet jesli jest tylko jeden) i wywala błąd
