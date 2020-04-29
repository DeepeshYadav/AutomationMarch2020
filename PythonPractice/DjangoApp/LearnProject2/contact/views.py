from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.

# register method without messages
def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, 'login successfully')
            return redirect("/")
        else:
            messages.info(request, 'Invalid Credentials')
            redirect(login)
    else:
        return render(request, "login.html")

'''
def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=first_name).exist():
                print("Username taken")
            elif User.objects.filter(email=email).exist():
                print("Email taken")
            else:
                user = User.objects.create_user(username=first_name,  password=password1, first_name=first_name, last_name= last_name, email=email)
                user.save();
                print("User Created")

        else:
            print("Password is not matching")
        return redirect('/')
    else:
        return render(request, 'register.html')
'''

# register method with messages to be print on UI
def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=first_name).exists():
                messages.info(request, "Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=first_name,  password=password1, first_name=first_name, last_name= last_name, email=email)
                user.save();
                messages.info(request, "User Created")
                return redirect('login')

        else:
            messages.info(request, "Password is not matching")
            return redirect('register')

        return redirect('/')
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')