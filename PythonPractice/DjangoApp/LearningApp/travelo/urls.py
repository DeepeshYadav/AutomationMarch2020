from django import urls
from . import views
from django.urls import path


urlpatterns = [
    path('', views.travelo_home, name='travel_home'),
]