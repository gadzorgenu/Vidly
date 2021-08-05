from django.db import models
# Creatng apis
from tastypie.resources import ModelResource
from movies.models import Movie


# Create your models here.
class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
        # not showing the date created field
        excludes = ['date_created']
