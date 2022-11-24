from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# Create your models here.
class Article(models.Model):

    title = models.CharField(max_length=250)
    sneak_peek = models.CharField(blank = True, max_length=300)
    content_pl = models.TextField(blank = True)
    content_eng = models.TextField(blank = True)
    date_posted = models.DateTimeField(default = datetime.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_img = models.ImageField(blank = True, upload_to = 'blog_pcs')

    def get_absolute_url(self):
        return reverse('article-detail', kwargs = {'pk' : self.pk})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        blog_img = Image.open(self.blog_img.path)

        if blog_img.height > 300 or blog_img.width > 300:
            output_size = (300, 300)
            blog_img.thumbnail(output_size)
            blog_img.save(self.blog_img.path)
