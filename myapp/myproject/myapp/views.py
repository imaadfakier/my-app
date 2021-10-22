# from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect, render
from .models import Restaurant


# Create your views here.
def index(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'index.html', {'restaurants': restaurants})


def counter(request):
    posts = [1, 2, 3, 4, 5, 'Tim', 'Tom', 'John']
    return render(request, 'counter.html', {'posts': posts})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email_address = request.POST['email']
        password = request.POST['password']
        password_re_entered = request.POST['password-repeat']
        if password == password_re_entered:
            if User.objects.filter(email=email_address).exists():
                messages.info(request, 'Email is already in use!')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already in use!')
                return redirect('register')
            else:
                new_user = User.objects.create_user(
                    username=username, 
                    email=email_address, 
                    password=password
                )
                new_user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match!')
            return redirect('register')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        logged_in_user = auth.authenticate(username=username, password=password)
        if logged_in_user is not None:
            auth.login(request, logged_in_user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid login details!')
            return redirect('/login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def post(request, pk):
    return render(request, 'post.html', {'pk': pk})