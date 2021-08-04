from django.urls import path
from . import views

# mapping urls
urlpatterns = [
    # path('') : representing the root of the app
    path('', views.index, name='index')
]
