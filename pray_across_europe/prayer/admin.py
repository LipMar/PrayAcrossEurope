from django.contrib import admin
from .models import Prayer, Country, Church, Prayer_Text

# Register your models here.
admin.site.register(Country)
admin.site.register(Church)
admin.site.register(Prayer_Text)
admin.site.register(Prayer)
