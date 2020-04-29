from django import urls
from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.html_home, name='html_home'),
    path('dindex/', views.dynamic_home, name='dhtml_home'),
    path('base/', views.dynamic_home_base, name='dhtml_home_base'),
    path('home/', views.addition, name='addition'),
    path('home/add/', views.add, name='add')

]