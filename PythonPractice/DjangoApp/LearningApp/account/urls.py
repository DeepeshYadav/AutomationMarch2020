from django import urls
from . import views
from django.urls import path


urlpatterns = [
    path('register', views.register, name='register'),
]