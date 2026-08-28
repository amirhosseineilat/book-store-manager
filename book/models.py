from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    publish_date = models.DateField()
    price = models.FloatField()
    page = models.IntegerField()
    favorites = models.ManyToManyField(User, related_name="favorites")
    genre = models.ManyToManyField(User, related_name="categories")


