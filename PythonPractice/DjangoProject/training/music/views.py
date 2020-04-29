from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
# Create your views here.

def display(request):
    datas = Album.objects.all()
    data_list = ''
    for data in datas:
        data_list = data_list + "  |:|  " + data.album_name
    return HttpResponse(data_list)




