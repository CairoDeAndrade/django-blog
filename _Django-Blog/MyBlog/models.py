from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Myblog(models.Model):
    subject = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    images = models.ImageField(blank=True, upload_to='photos/%Y/%m')
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.category
