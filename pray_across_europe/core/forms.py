from django import forms
from django.conf import settings
from django.core.mail import send_mail
import smtplib

class ContactForm(forms.Form): # dodac subject i zoabzcyc dlaczego nie wyswietla sie tresc wiadomosci
    imie = forms.CharField(max_length=100)
    email = forms.EmailField()
    temat = forms.CharField(max_length = 70)
    wiadomosc = forms.CharField(widget=forms.Textarea)

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('imie').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('temat')

        msg = f"\n{name} with email {from_email} said:\n{subject}\n\n" #\n powodują wyświetlanie sie linii
        msg += cl_data.get('wiadomosc')

        print(msg)
        print(subject)

        return subject, msg

    def send(self):
        subject, msg = self.get_info()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('mklipki@gmail.com', 'quxzaigpexrvklgo')
        server.sendmail('mklipki@gmail.com', 'pray.across.europe@gmail.com', msg)
