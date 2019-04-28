from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from .models import Student

@csrf_exempt
def profile(request, userID):
    if request.method == "GET":
        stu = Student.objects.get(stu_id = userID)
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
        return render_to_response('stu/personal-profile.html', locals())
        #return render(request, 'stu/personal-profile.html', {'gender':gender, 'name':name, 'phone':phone, 'email':json.dumps(email), 'university':university, 'major':major}) #, {'gender': gender}
    elif request.method == "POST":
        return redirect('/stu/editor/%s' %userID) 
    else:
        return render(request, 'stu/personal-profile.html')

@csrf_exempt
def editor(request, userID):
    if request.method == "POST":
        message = "You should agree with the privacy of Exam and Application System"
        check_box = request.POST.getlist('check_box')
        if check_box:        
            genderSet = {"male":0, "female":1}
            stu = Student.objects.get(stu_id=userID)
            if request.POST.get('firstName') != "":
                stu.stu_fname = request.POST.get('firstName')
            if request.POST.get('lastName') != "":    
                stu.stu_lname = request.POST.get('lastName')
            if request.POST.get('phoneNum') != "":    
                stu.stu_phone = request.POST.get('phoneNum')
            if request.POST.get('university') != "":     
                stu.stu_c_uni = request.POST.get('university')
            if request.POST.get('major') != "": 
                stu.stu_major = request.POST.get('major')

            if request.POST.get('gender') != "":
                gender = str(request.POST.get('gender'))
                gender = gender.lower()
                if genderSet.__contains__(gender) == True:
                    stu.stu_gender = genderSet.get(gender)
            
            stu.save()
            return redirect('/stu/profile/%s' %userID) 
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