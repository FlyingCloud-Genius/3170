from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
import json

# Create your views here.
from .models import Student

def profile(request, userEamil):
    if request.method == "GET":
        stu = Student.objects.get(stu_email = userEamil)
        # print("gender: ")
        # print(stu.stu_gender)
        name = stu.stu_fname + stu.stu_lname
        if stu.stu_gender == 0:
            gender = "Male"
        elif stu.stu_gender == 1:
            gender = "Female"
        else:
            gender = None
        phone = stu.stu_phone
        email = stu.stu_email
        university = stu.stu_c_uni
        major = stu.stu_major
        #return render_to_response('stu/personal-profile.html', locals())
        return render(request, 'stu/personal-profile.html', {'gender':gender, 'name':name, 'phone':phone, 'email':email, 'university':university, 'major':major}) #, {'gender': gender}

    return render(request, 'stu/personal-profile.html')


def editor(request, userEamil):
    if request.method == "POST":
        message = "You should agree with the privacy of Exam and Application System"
        check_box = request.POST.getlist('check_box')
        if check_box:        
            genderSet = {0:"male", 1:"female"}
            stu = Student.objects.get(stu_email=userEamil)
            stu.stu_fname = request.POST.get('firstName')
            stu.stu_lname = request.POST.get('lastName')
            stu.stu_phone = request.POST.get('phoneNum')
            stu.stu_c_uni = request.POST.get('university')
            stu.stu_major = request.POST.get('major')

            gender = str(request.POST.get('gender'))
            gender = gender.lower()
            if genderSet.__contains__(gender) == True:
                stu.stu_gender = genderSet[gender]
            
            stu.save()
            print(stu.stu_gender)
            return redirect('/stu/profile/%s' %userEmail) 
        return render(request, 'stu/personal-edit.html', {"message": message}) 
            


        
        

    return render(request, 'stu/personal-edit.html')


def application(request):
    pass
    return render(request, 'stu/application.html')


def exercise(request):
    pass
    return render(request, 'stu/exercise.html')


def exams(request):
    pass
    return render(request, 'stu/tables-exams.html')


def grades(request):
    pass
    return render(request, 'stu/tables-grades.html')