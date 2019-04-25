#-*- conding:utf-8 -*-
from django.contrib import auth
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from django.contrib import messages

# Create your views here.
from .models import Info
from .forms import InfoForm


def login(request):
    if request.method == "POST":
        userEmail = request.POST.get('userEmail')
        password = request.POST.get('password')
        message = "All forms should be filled!"
        # print(type(userEmail))
        # print(type(password))
        if userEmail != "" and password != "":
            # print(userEmail + " " + password)
            # print(type(userEmail))
            try:
                user = Info.objects.get(reg_id = userEmail)
                if user.reg_password == password:
                    return render(request, 'reg/index.html')
                else:
                    message = "Incorrect password!"
            except:
                message = "Account doesn't exist!"
        return render(request, 'reg/login.html', {"message": message})
    return render(request, 'reg/login.html')


def index(request):
    print("123hhhhhhhhhhhhhhhhhhhh")
    pass
    return render(request, 'reg/index.html')


def register(request):
    if request.method == "POST":
        userEmail = request.POST.get('userEmail')
        password = request.POST.get('password')
        repPassword = request.POST.get('reppassword')
        userName = request.POST.get('userName')
        phone = request.POST.get('phoneNum')
        message = "Please complete the forms of Email and password!"

        if userEmail != "" and password != "" and repPassword != "":        #check if user doesn't complete his/her form 
            if password == repPassword:                                     #check if the two passwords are differents 
                #Info.objects.create(reg_id=userEmail, reg_password=password)
                print(userEmail + " " + password)
                return render(request, 'reg/login.html')
            else:
                message = "Your second password is not match, please try again."
        return render(request, 'reg/register.html', {"message": message})
    return render(request, 'reg/register.html')
