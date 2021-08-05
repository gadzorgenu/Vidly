from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
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

    # movie = Movie.objects.get(pk=movie_id) OR pass the Movie class to the get_object_or_404 exception
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, template_name='movies/detail.html', context={'movie': movie})
