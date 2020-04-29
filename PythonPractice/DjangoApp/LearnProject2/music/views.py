from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
# Create your views here.

def display(request):
    all_data = Album.objects.all()
    return HttpResponse(all_data)
