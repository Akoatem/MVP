from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import *
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# create the register method

def register(request):
    # use POST to create user in the database
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        # check for password
        if password1 == password2:
            # check for username
            if User.objects.filter(username=username).exists():
                #print('Usernamme taken')
                messages.info(request,'Username taken')
                return redirect('register')
            # check for email
            elif User.objects.filter(email=email).exists():
                #print('Email taken') 
                messages.info(request,'Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                email=email, password=password1)
            
                user.save();
                print('user created')
                return redirect('login')
        else:
            #print('Password mismatch')
            messages.info(request,'Password Mismatch')
            return redirect('register')
        return redirect('/') # it will redirect back to home page
    
    else:
        return render(request, 'register.html' )


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            
            
    else:
        return render(request, 'login.html' )
    
    
def logout(request):
        auth.logout(request)
        return redirect('/')