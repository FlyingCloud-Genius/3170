#-*- conding:utf-8 -*-
import time
from django.contrib import auth
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from .models import RegInfo
from stu.models import Student, StuPhones
from uni.models import University
from guardian.models import Guardian
# from .forms import InfoForm


def login(request):
    if request.method == "POST":
        accountType = request.POST.get('accountType')
        userEmail = request.POST.get('userEmail')
        password = request.POST.get('password')
        message = "Please select your account type!"
        print(accountType)
        # print(type(userEmail))
        # print(type(password))
        if accountType != "I am" and accountType != None: 
            if userEmail != "" and password != "":
                try:
                    user = RegInfo.objects.get(reg_id = userEmail)
                    if user.reg_password == password:
                        if accountType == "Student":
                            if Student.objects.filter(stu_email=userEmail).exists() == True:
                                return redirect('/stu/profile') #render(request, 'reg/index.html')
                            else:
                                message = "This account is not a sutdent!"
                        elif accountType == "University":
                            if University.objects.filter(uni_email=userEmail).exists() == True:                            
                                return redirect('/uni/profile')
                            else:
                                message = "This account is not a university!"
                        elif accountType == "Guardian":
                            if Guardian.objects.filter(guardian_email=userEmail).exists() == True:                            
                                return redirect('/guardian/profile')
                            else:
                                message = "This account is not a guardian!"                           
                    else:
                        message = "Incorrect password!"
                except:
                    message = "Account doesn't exist!"
            else:
                message = "All forms should be filled!"
        return render(request, 'reg/login.html', {"message": message})
    return render(request, 'reg/login.html')


def index(request):
    print("123hhhhhhhhhhhhhhhhhhhh")
    pass
    return render(request, 'reg/index.html')


def register(request):
    if request.method == "POST":
        accountType = request.POST.get('accountType')
        userEmail = request.POST.get('userEmail')
        password = str(request.POST.get('password'))
        repPassword = str(request.POST.get('reppassword'))
        userName = request.POST.get('userName')
        phone = str(request.POST.get('phoneNum'))
        message = "Please select your account type!"
        print("accounttype:")
        print(accountType)
        if accountType != "I am" and accountType != None:           
            if userEmail != "" and password != "" and repPassword != "" and userName != "" and phone != None: #check if user doesn't complete his/her form
                if "@" in userEmail:                                                        #check if this is a formal E-mail formate
                    if RegInfo.objects.filter(reg_id=userEmail).exists() == False:          #check if the account had existed
                        if password == repPassword:                                         #check if the two passwords are differents 
                            print(userEmail + " " + password)
                            if accountType == "Student":
                                sid = "0" + time.strftime("%Y%m%d%H%M%S", time.localtime()) 
                                print(sid)
                                Reg = RegInfo.objects.create(reg_id=userEmail, reg_password=password)
                                Stu = Student.objects.create(stu_id=sid, stu_email=userEmail, stu_name=userName, reg=Reg)
                                StuPhones.objects.create(stu=Stu, stu_phone=phone)
                                return redirect('login')
                               
                            elif accountType == "University":
                                uid = "1" + time.strftime("%Y%m%d%H%M%S", time.localtime()) 
                                print(uid)
                                Reg = RegInfo.objects.create(reg_id=userEmail, reg_password=password)
                                Uni = University.objects.create(uni_id=uid, uni_email=userEmail, uni_name=userName, uni_phone=phone, reg=Reg)
                                return redirect('login')                                
                            elif accountType == "Guardian":
                                gid = "2" + time.strftime("%Y%m%d%H%M%S", time.localtime())
                                print(gid)
                                Reg = RegInfo.objects.create(reg_id=userEmail, reg_password=password)
                                Gua = Guardian.objects.create(guardian_id=gid, guardian_email=userEmail, guard_name=userName, guardian_phone=phone, reg=Reg) 
                                return redirect('login')                                                     
                        else:
                            message = "Your second password is not match, please try again."
                    else:
                        message = "The account is already exist!"
                else:
                    message = "Please enter correct E-mail format."
            else:
                message = "Please complete the forms of Email and password!"
        return render(request, 'reg/register.html', {"message": message})
    return render(request, 'reg/register.html')
