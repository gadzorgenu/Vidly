from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

# Create your views here.


def index(request):

    # retrieving all movies
    # SQL COMMAND:  SELECT * FROM movies_movie
    movies = Movie.objects.all()

    # formatting the response as a string
    # output = ', '.join([m.title for m in movies])

    # filtering movies
    # SQL COMMAND:  SELECT * FROM movies_movie WHERE release_year=2021
    # Movie.objects.filter(release_year=2021)

    # retrieving one object
    # Movie.objects.get(id=1)

    # return HttpResponse(output)

    return render(request, template_name='movies/index.html', context={'movies': movies})


def detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request, template_name='movies/detail.html', context={'movie': movie})
