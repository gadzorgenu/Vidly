from django.utils import timezone
from django.db import models
import json
from pathlib import Path

# Create your models here.
# inheriting the Genre class from the base class


class Genre(models.Model):
    name = models.CharField(max_length=255)

# magic method ro represent the genre with it's name


def __str__(self):
    return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    # passing a reference to the now method
    date_created = models.DateTimeField(default=timezone.now)


# movies = [
#     {
#         'id': 1,
#         'title': 'Terminator',
#         'release_year': 1957,
#         'number_in_stock': 3,
#         'daily_rate': 1.57,
#         'genre': 'Action',
#         'date_created': '2021-08-04 21:20:45'
#     },
#     {
#         'id': 2,
#         'title': 'TerminatorX',
#         'release_year': 1967,
#         'number_in_stock': 4,
#         'daily_rate': 2.57,
#         'genre': 'Action',
#         'date_created': '2021-08-04 21:20:45'
#     },
#     {
#         'id': 3,
#         'title': 'Terminator2',
#         'release_year': 1987,
#         'number_in_stock': 5,
#         'daily_rate': 2.57,
#         'genre': 'Action',
#         'date_created': '2021-08-04 21:20:45'
#     },
# ]


# data = json.dumps(movies)

# Path('movies.json').write_text(data)
