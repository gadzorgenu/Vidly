from django.urls import path
from . import views

# mapping urls
urlpatterns = [
    # path('') : representing the root of the app
    path('', views.index, name='movies_index'),
    # we use <paramName> to define url params
    path('<int:movie_id>', views.detail, name='movies_detail')
]
