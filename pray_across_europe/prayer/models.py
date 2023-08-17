#-*- coding:utf-8 -*-
from django.db import models
from PIL import Image


# Create your models here.
class Country(models.Model):
    country_pl = models.CharField(max_length= 100, blank = True, null = True)
    country_eng = models.CharField(max_length=100, blank = True, null = True)
    country_local = models.CharField(max_length=100, blank = True, null = True)

    def __str__(self):
        return self.country_pl

class Church(models.Model):
    church_pl = models.CharField(max_length=150, blank = True, null = True)
    church_eng = models.CharField(max_length=150, blank = True, null = True)
    church_local = models.CharField(max_length=150, blank = True, null = True)

    def __str__(self):
        return self.church_pl

class Prayer_Text(models.Model):
    prayer_text_pl = models.TextField(blank = True, null = True)
    prayer_text_eng = models.TextField(blank = True, null = True)
    prayer_text_local = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.prayer_text_pl

class Prayer(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank = True, null = True)
    date1 = models.DateField(blank = True, null = True)
    date2 = models.DateField(blank = True, null = True)
    date3 = models.DateField(blank = True, null = True)
    date4 = models.DateField(blank = True, null = True)
    prayer_text = models.ForeignKey(Prayer_Text, on_delete=models.DO_NOTHING, blank = True, null = True) #czy beda 3 wersje językowe i jak to ma sie wyswietlac prayer = models.ForeignKey(Prayer_Text)
    flag = models.ImageField(blank = True, upload_to = 'flag_pcs')
    church_img = models.ImageField(blank = True, upload_to = 'church_img_pcs')
    church = models.ForeignKey(Church, on_delete = models.DO_NOTHING, blank = True, null = True) #jesli 3 wersje jezykowe to osobna klasa a tutaj church_description jako foreign key)


    def __str__(self):
        return self.country.country_pl

    def save(self, *args, **kwargs):
        super().save(*args, ** kwargs)
        flag = Image.open(self.flag.path)
        church_img = Image.open(self.church_img.path)

        if flag.height > 300 or flag.width > 450:
            output_size = (100, 250)
            flag.thumbnail(output_size)
            flag.save(self.flag.path)
        elif church_img.height > 300 or church_img.width > 450:
            output_size = (300, 450)
            church_img.thumbnail(output_size)
            church_img.save(self.church_img.path)

class Counter(models.Model):
    counter_img = models.ImageField(blank = True, upload_to = 'counter_pcs')
'''
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        counter_img = Image.open(self.counter_img.path)

        if counter_img.height > 300 or counter_img.width > 300:
            output_size = (300, 300)
            counter_img.thumbnail(output_size)
            counter_img.save(self.counter_img.path)
'''