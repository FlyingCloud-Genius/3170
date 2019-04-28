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

        enrollLink = "../enrollment/" + userID
        exeLink = "../exercise/" + userID
        exeVerLink = "../exercise/" + userID + "#verbal"
        exeQuaLink = "../exercise/" + userID + "#quantitative"
        exeWriLink = "../exercise/" + userID + "#writing"
        appLink = "../application/" + userID
        appUSALink = "../application/" + userID + "#usa"
        appEURLink = "../application/" + userID + "#europe"
        appASILink = "../application/" + userID + "#asia"
        appOthLink = "../application/" + userID + "#others"       
        return render_to_response('stu/personal-profile.html', locals())
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


def application(request, userID):
    if request.method == "GET":
        stu = Student.objects.get(stu_id=userID)

        name = stu.stu_fname + stu.stu_lname
        proLink = "../profile/" + userID
        enrollLink = "../enrollment/" + userID
        exeLink = "../exercise/" + userID
        exeVerLink = "../exercise/" + userID + "#verbal"
        exeQuaLink = "../exercise/" + userID + "#quantitative"
        exeWriLink = "../exercise/" + userID + "#writing"
        appLink = "../application/" + userID
        appUSALink = "../application/" + userID + "#usa"
        appEURLink = "../application/" + userID + "#europe"
        appASILink = "../application/" + userID + "#asia"
        appOthLink = "../application/" + userID + "#others"       
        return render_to_response('stu/application.html', locals())
    return render(request, 'stu/application.html')


def exercise(request, userID):
    if request.method == "GET":
        stu = Student.objects.get(stu_id=userID)

        name = stu.stu_fname + stu.stu_lname
        proLink = "../profile/" + userID
        enrollLink = "../enrollment/" + userID
        exeLink = "../exercise/" + userID
        exeVerLink = "../exercise/" + userID + "#verbal"
        exeQuaLink = "../exercise/" + userID + "#quantitative"
        exeWriLink = "../exercise/" + userID + "#writing"
        appLink = "../application/" + userID
        appUSALink = "../application/" + userID + "#usa"
        appEURLink = "../application/" + userID + "#europe"
        appASILink = "../application/" + userID + "#asia"
        appOthLink = "../application/" + userID + "#others"       
        return render_to_response('stu/exercise.html', locals())
    return render(request, 'stu/exercise.html')


def exams(request, userID):
    if request.method == "GET":
        stu = Student.objects.get(stu_id=userID)

        name = stu.stu_fname + stu.stu_lname
        proLink = "../profile/" + userID
        enrollLink = "../enrollment/" + userID
        exeLink = "../exercise/" + userID
        exeVerLink = "../exercise/" + userID + "#verbal"
        exeQuaLink = "../exercise/" + userID + "#quantitative"
        exeWriLink = "../exercise/" + userID + "#writing"
        appLink = "../application/" + userID
        appUSALink = "../application/" + userID + "#usa"
        appEURLink = "../application/" + userID + "#europe"
        appASILink = "../application/" + userID + "#asia"
        appOthLink = "../application/" + userID + "#others"       
        return render_to_response('stu/tables-exams.html', locals())
    return render(request, 'stu/tables-exams.html')


def grades(request, userID):
    if request.method == "GET":
        stu = Student.objects.get(stu_id=userID)

        name = stu.stu_fname + stu.stu_lname
        proLink = "../profile/" + userID
        enrollLink = "../enrollment/" + userID
        exeLink = "../exercise/" + userID
        exeVerLink = "../exercise/" + userID + "#verbal"
        exeQuaLink = "../exercise/" + userID + "#quantitative"
        exeWriLink = "../exercise/" + userID + "#writing"
        appLink = "../application/" + userID
        appUSALink = "../application/" + userID + "#usa"
        appEURLink = "../application/" + userID + "#europe"
        appASILink = "../application/" + userID + "#asia"
        appOthLink = "../application/" + userID + "#others"       
        return render_to_response('stu/tables-grades.html', locals())
    return render(request, 'stu/tables-grades.html')