from django.shortcuts import render

# Create your views here.

def travelo_home(request):
    return render(request, 'index.html')