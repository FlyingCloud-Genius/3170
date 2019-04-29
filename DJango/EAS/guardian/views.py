from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from .models import Guardian

@csrf_exempt
def profile(request, userID):
    if request.method == "GET": 
        guardian = Guardian.objects.get(guardian_id = userID)
        name = guardian.guardian_fname + " " + guardian.guardian_lname
        phone = guardian.guardian_phone
        email = guardian.guardian_email

        ProfileLink = "../profile/" + userID
        ExercisesLink = "../exercises/" + userID
        GradesLink = "../grades/" + userID
        ExamsLink = "../exams/" + userID
        return render_to_response('guardian/guardian-profile.html', locals())
    elif request.method == 'POST':
        print("7777777777777777777777777777")
        return redirect('/guardian/editor/%s' %userID)
    else:
        print("666666666666666666666666666")
        return render(request, 'guardian/guardian-profile.html')

@csrf_exempt
def editor(request, userID):
    print(userID)
    print("111111111111111111111111111")
    if request.method == "POST":
        print("222222222222222222222222222222")
        message = "You should agree with the privacy of Exam and Application System"
        check_box = request.POST.getlist('check_box')
        print("333333333333333333333333333333")
        if check_box: 
            print(userID)       
            guardian = Guardian.objects.get(guardian_id=userID)
            if request.POST.get('firstName') != "":
                guardian.guardian_fname = request.POST.get('firstName')
            if request.POST.get('lastName') != "":    
                guardian.guardian_lname = request.POST.get('lastName')
            if request.POST.get('phoneNum') != "":    
                guardian.guardian_phone = request.POST.get('phoneNum')   
            guardian.save()
            print("444444444444444444444444444444444444")
            return redirect('/guardian/profile/%s' %userID) 
        return render(request, 'guardian/guardian-edit.html', {"message": message}) 
    return render(request, 'guardian/guardian-edit.html')

def exams(request, userID):
    if request.method == "GET":
        guardian = Guardian.objects.get(guardian_id=userID)

        name = guardian.guardian_fname + guardian.guardian_lname
        ProfileLink = "../profile/" + userID
        ExercisesLink = "../exercises/" + userID
        GradesLink = "../grades/" + userID
        ExamsLink = "../exams/" + userID
        return render_to_response('guardian/tables-exams-guard.html', locals())
    return render(request, 'guardian/tables-exams-guard.html')


def exercises(request, userID):
    if request.method == "GET":
        guardian = Guardian.objects.get(guardian_id=userID)

        name = guardian.guardian_fname + guardian.guardian_lname
        ProfileLink = "../profile/" + userID
        ExercisesLink = "../exercises/" + userID
        GradesLink = "../grades/" + userID
        ExamsLink = "../exams/" + userID
        return render_to_response('guardian/tables-exercises-guard.html', locals())
    return render(request, 'guardian/tables-exercises-guard.html')


def grades(request, userID):
    if request.method == "GET":
        guardian = Guardian.objects.get(guardian_id=userID)

        name = guardian.guardian_fname + guardian.guardian_lname
        ProfileLink = "../profile/" + userID
        ExercisesLink = "../exercises/" + userID
        GradesLink = "../grades/" + userID
        ExamsLink = "../exams/" + userID
        return render_to_response('guardian/tables-grades-guard.html', locals())
    return render(request, 'guardian/tables-grades-guard.html')