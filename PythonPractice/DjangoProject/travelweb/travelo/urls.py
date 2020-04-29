
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('index/register', views.register, name='register'),
    path('index/login', views.login, name='login'),
    path('index/logout', views.logout, name='logout'),
]
