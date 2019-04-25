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
    pass
    return  render(request, 'reg/register.html')



#def login(request):
#    if request.method == 'GET':
#        return render(request, 'reg/login.html')

#    if request.method == 'POST':

#        # 如果登录成功，绑定参数到cookie中，set_cookie
#        name = request.POST.get('name')
#        password = request.POST.get('password')
#        # 查询用户是否在数据库中
#        if Info.objects.filter(u_name=name).exists():
#            Info = Info.objects.get(u_name=name)
#            if check_password(password, Info.u_password):
#                return render(request, 'reg/index.html') #'/stu/index/'
#            else:
#            # return HttpResponse('用户密码错误')
#                return render(request, 'reg/index.html', {'password': 'password wrong'})
#        else:
#            # return HttpResponse('用户不存在')
#            return render(request, 'reg/index.html', {'name': 'account does not exist'})


#def register(request):
#    if request.method == 'GET':
#        return render(request, 'reg/login.html')
#    if request.method == 'POST':
#        # 注册
#        #userType = request.POST.get('')
#        userEmail = request.POST.get('userEmail')
#        password = request.POST.get('password')
#        repPassword = request.POST.get('reppassword')
#        if name != "" and password != "" and repPassword !="":
#            # 对密码进行加密
#            #Info.objects.create(u_name=name, u_password=password)
#            print("new id = " + userEmail + " password = " + password + "repeat password" + repPassword)
#            print(Info.objects.all())
#            return render(request, 'reg/index.html')
#        else:
#            messages.error(request, 'QQQ')
#            print("wrong!")
#            return render(request, 'reg/register.html')