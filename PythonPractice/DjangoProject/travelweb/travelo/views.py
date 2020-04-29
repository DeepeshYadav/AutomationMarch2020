from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth, User
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, "Login Successful")
            return redirect("/index")
        else:
            messages.info(request, "Invalid Credentials")
            return redirect("/index/login")
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "User already exist")
                return redirect('/index/register')
            else:
                obj = User.objects.create_user(username=firstname, first_name=firstname, last_name = last_name, email=email, password=password1)
                obj.save()
        else:
            messages.info(request, 'Password did not match')
            return redirect('/index/register')
        return redirect('/index')
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/index')
