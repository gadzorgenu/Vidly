from django.urls import path
from . import views


app_name = 'movies'
# mapping urls
urlpatterns = [
    # path('') : representing the root of the app
    path('', views.index, name='index'),
    # we use <paramName> to define url params
    path('<int:movie_id>', views.detail, name='detail')
]
