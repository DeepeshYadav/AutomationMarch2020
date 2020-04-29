from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.

def home(request):
    return HttpResponse("<h1>Hello world</h1>")

def home_index(request):
    return render(request, 'home.html', {'name':'Harish'})

def home_base(request):
    return render(request, 'home_base.html', {'name':'Veera'})

def addition(request):
    return render(request, 'addition.html')

def result(request):
    number1 = request.GET['num1']
    number2 = request.GET['num2']
    resultdata = int(number1) + int(number2)
    return render(request, 'result.html', { 'result': resultdata })

def get_user_data(request):
    return render(request, 'getdata_post.html')

def display_user_data(request):
    first_name = request.POST['fname']
    last_name = request.POST['lname']
    email_id = request.POST['email']
    address = request.POST['address']
    mobile_no = request.POST['mobile']
    user_data = {}
    user_data['first_name'] = first_name
    user_data['last_name'] = last_name
    user_data['email_id'] = email_id
    user_data['address'] = address
    user_data['mobile_no'] = mobile_no
    return render(request, 'display_post.html', user_data)


dest1 = Destination()
dest1.name = 'Mumbai'
dest1.desc  = "Bollywood City"
dest1.price = 800

def travelo(request):
    return render(request, 'index.html', {'dest1' : dest1})


dest2 = Destination()
dest2.name = 'Mumbai'
dest2.desc  = "Bollywood City"
dest2.price = 800
dest2.img  = 'destination_1.jpg'
dest2.offer = True

dest3 = Destination()
dest3.name = 'Banglore'
dest3.desc  = "IT Hub City"
dest3.price = 900
dest3.img  = 'destination_2.jpg'
dest3.offer =  False

dest4 = Destination()
dest4.name = 'Jaipur'
dest4.desc  = "Pink City"
dest4.price = 1000
dest4.img  = 'destination_3.jpg'
dest4.offer = True


dests = [ dest2, dest3, dest4]
def travelo_multi(request):
    return render(request, 'index_loop.html', {'dests' : dests})
