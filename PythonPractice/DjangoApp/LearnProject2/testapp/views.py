from django.shortcuts import render
from .models import Destination
# Create your views here.

dest1 = Destination()
dest2= Destination()
dest3 = Destination()

dest1.name = 'Mombai'
dest1.price = '800'
dest1.desc = "The city which never sleep"
dest1.img = 'destination_1.jpg'
dest1.offer = False

dest2.name = 'Jaipur'
dest2.price = '900'
dest2.desc = "The Pink City"
dest2.img = 'destination_2.jpg'
dest2.offer = True

dest3.name = 'Delhi'
dest3.price = '100'
dest3.desc = "Heart Of India"
dest3.img = 'destination_3.jpg'
dest3.offer = False

# def home(request):
#     return render(request, 'index.html')

def index(request):
     return render(request, 'index.html', {'dest1' : dest1, 'dest2' : dest2, 'dest3' : dest3})

dests = [dest1, dest2, dest3]
def home(request):
    return render(request, 'home.html', {'dests': dests})