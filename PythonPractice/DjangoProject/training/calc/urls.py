from django import urls
from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.home_index, name='home_index'),
    path('home_base/', views.home_base, name='home_base'),
    path('addition/', views.addition, name='addition'),
    path('addition/result', views.result, name='result'),
    path('userdata/', views.get_user_data, name='userdata'),
    path('userdata/display', views.display_user_data, name='displaydata'),
    path('travelo/', views.travelo, name='travelo'),
    path('travelo_multi/', views.travelo_multi, name='travelo_multi')

]

