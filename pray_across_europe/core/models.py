#-*- coding:utf-8 -*-
from django.db import models
from django import forms
from django.conf import settings
from django.core.mail import send_mail

# Create your models here.

class Contact(models.Model): #zmienic na angielskie nazwy i dodac subject
    imie = models.CharField(blank = True,max_length=100)
    email = models.EmailField()
    temat = models.CharField(blank = True,max_length = 70)
    wiadomosc = models.TextField()

    def __str__(self):
        return self.email


class Downloads(models.Model):
    download_file = models.FileField(blank = True, upload_to='documents')
    name = models.CharField(blank = True, max_length = 100)
    icon = models.ImageField(blank = True)
    #picture = models.ImageField(blank = True) #czy tutaj powinien byc upload_to = 'document' skoro jest na górze?