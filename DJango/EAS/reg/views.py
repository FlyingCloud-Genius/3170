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
from stu.models import Student
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
                                stu = Student.objects.get(stu_email = userEmail)
                                stuID = stu.stu_id
                                return redirect('/stu/profile/%s' %stuID) #render(request, 'reg/index.html')
                            else:
                                message = "This account is not a sutdent!"
                        elif accountType == "University":
                            if University.objects.filter(uni_email=userEmail).exists() == True:    
                                uni = University.objects.get(uni_email = userEmail)
                                return redirect('/uni/profile/%s' %uni.uni_email)
                            else:
                                message = "This account is not a university!"
                        elif accountType == "Guardian":
                            if Guardian.objects.filter(guardian_email=userEmail).exists() == True:                            
                                guardian = Guardian.objects.get(guardian_email = userEamil)
                                guardianID = guardian.guardian_id
                                return redirect('/guardian/profile/%s' %guardianID)
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
        check_box = request.POST.getlist('check_box')
        accountType = request.POST.get('accountType')
        userEmail = request.POST.get('userEmail')
        password = str(request.POST.get('password'))
        repPassword = str(request.POST.get('reppassword'))
        message = "You should agree with the privacy of Exam and Application System!"
        if check_box:
            if accountType != "I am" and accountType != None:           
                if userEmail != "" and password != "" and repPassword != "":                    #check if user doesn't complete his/her form
                    if "@" in userEmail:                                                        #check if this is a formal E-mail formate
                        if RegInfo.objects.filter(reg_id=userEmail).exists() == False:          #check if the account had existed
                            if password == repPassword:                                         #check if the two passwords are differents 

                                if accountType == "Student":
                                    sid = "0" + time.strftime("%Y%m%d%H%M%S", time.localtime()) 
                                    #print(sid)
                                    Reg = RegInfo.objects.create(reg_id=userEmail, reg_password=password)
                                    Stu = Student.objects.create(stu_id=sid, stu_email=userEmail, reg=Reg)
                                    return redirect('../stu/editor/%s' %sid)
                                
                                elif accountType == "University":
                                    uid = "1" + time.strftime("%Y%m%d%H%M%S", time.localtime()) 
                                    #print(uid)
                                    Reg = RegInfo.objects.create(reg_id=userEmail, reg_password=password)
                                    Uni = University.objects.create(uni_id=uid, uni_email=userEmail, reg=Reg)
                                    return redirect('login')

                                elif accountType == "Guardian":
                                    gid = "2" + time.strftime("%Y%m%d%H%M%S", time.localtime())
                                    #print(gid)
                                    Reg = RegInfo.objects.create(reg_id=userEmail, reg_password=password)
                                    Gua = Guardian.objects.create(guardian_id=gid, guardian_email=userEmail, reg=Reg) 
                                    return redirect('../guardian/editor/%s' %gid)                                                     
                            else:
                                message = "Your second password is not match, please try again."
                        else:
                            message = "The account is already exist!"
                    else:
                        message = "Please enter correct E-mail format."
                else:
                    message = "Please complete the forms of Email and password!"
            else:
                message = "Please select your account type!"
        return render(request, 'reg/register.html', {"message": message})
    return render(request, 'reg/register.html')
