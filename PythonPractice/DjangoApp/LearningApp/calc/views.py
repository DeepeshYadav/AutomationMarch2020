from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("<h1>Hello World</h1>")


def html_home(request):
    return render(request, 'index_home.html')

def dynamic_home(request):
    return render(request, 'index_dynamic.html', {'name':'Deepesh'})


def dynamic_home_base(request):
    return render(request, 'index_with_base.html', {'name':'Rahul'})


def addition(request):
    return render(request, 'addition.html', {'name':'Rahul'})

def add(request):
    num1 = request.GET['num1']
    num2 = request.GET['num2']
    result = int(num1) + int(num2)
    return render(request, 'result.html', {'result':result})
