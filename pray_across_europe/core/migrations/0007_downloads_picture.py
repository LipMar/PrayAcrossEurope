# Generated by Django 4.0.6 on 2022-10-03 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_downloads_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='downloads',
            name='picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
