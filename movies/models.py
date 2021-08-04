from django.utils import timezone
from django.db import models

# Create your models here.
# inheriting the Genre class from the base class


class Genre(models.Model):
    name = models.CharField(max_length=255)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    # passing a reference to the now method
    date_created = models.DateTimeField(default=timezone.now)
