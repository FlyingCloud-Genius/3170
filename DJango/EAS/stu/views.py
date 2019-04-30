from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import json
import time
import os

# Create your views here.
from .models import Student, StuExam, AppliedExam, University, StuExercise, StuAnswerSheet, StuApplication

@csrf_exempt
def profile(request, userID):
    if request.method == "GET":
        appliedExam =  list(AppliedExam.objects.values_list('stu_id', 'exam_id'))
        unirawNameitems = sorted(list(University.objects.values_list('uni_name')))
        uniNameitems = []
        for obj in unirawNameitems:
            uniNameitems.append(obj[0])
        examitems = []
        examObject = StuExam.objects.all()
        for obj in appliedExam:
            if obj[0] == userID:
                for dd in examObject:
                    if dd.exam_id == obj[1]:
                        examitems += [dd.as_dict()]

        ansSheet = StuAnswerSheet.objects.all()
        ansRes = []
        for obj in ansSheet:
            if obj.examinee == userID and obj.ans_score:
                ansRes.append(obj)

        appliedApplication = StuApplication.objects.all()
        appliedAppRes = []
        for obj in appliedApplication:
            if obj.stu_id == userID:
                temp = {}
                temp.update(obj.as_dict())
                c = {'uniName':University.objects.get(uni_id=obj.apply_uni_id).uni_name}
                temp.update(c)
                appliedAppRes.append(temp)

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
        uploadURL = "../profile/uploadfile/" + userID      
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
        stu = Student.objects.get(stu_id=userID)
        stu.stu_fname = request.POST.get('firstName')
        stu.stu_lname = request.POST.get('lastName')
        if request.POST.get('firstName') != "" and request.POST.get('lastName') != "":
            if check_box:        
                genderSet = {"male":0, "female":1}
                # stu = Student.objects.get(stu_id=userID)
                # if request.POST.get('firstName') != "":
                #     stu.stu_fname = request.POST.get('firstName')
                # if request.POST.get('lastName') != "":    
                #     stu.stu_lname = request.POST.get('lastName')
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
        else:
            message = "First name and last name should be filled!" 
        return render(request, 'stu/personal-edit.html', {"message": message}) 
    return render(request, 'stu/personal-edit.html')


def application(request, userID):
    if request.method == "GET":
        university = University.objects.all()
        universityItem = list(university)

        stu = Student.objects.get(stu_id=userID)
        name = stu.stu_fname + stu.stu_lname
        proLink = "../profile/" + userID
        enrollLink = "../enrollment/" + userID
        exeLink = "../exercise/" + userID
        exeVerLink = "../exercise/" + userID + "#verbal"
        exeQuaLink = "../exercise/" + userID + "#quantitative"
        exeWriLink = "../exercise/" + userID + "#writing"
        appLink = "../application/" + userID  
        return render_to_response('stu/application.html', locals())
    return render(request, 'stu/application.html')


def exercise(request, userID):
    if request.method == "GET":
        allExercise = StuExercise.objects.all()
        verbalExercise = []
        quantitativeExercise = []
        writingExercise = []
        for obj in allExercise:
            if obj.que_type == "Verbal Reasoning":
                verbalExercise.append(obj)
            if obj.que_type == "Quantitative Reasoning":
                quantitativeExercise.append(obj)
            if obj.que_type == "Analytical Writing":
                writingExercise.append(obj)

        stu = Student.objects.get(stu_id=userID)
        name = stu.stu_fname + stu.stu_lname
        proLink = "../profile/" + userID
        enrollLink = "../enrollment/" + userID
        exeLink = "../exercise/" + userID
        exeVerLink = "../exercise/" + userID + "#verbal"
        exeQuaLink = "../exercise/" + userID + "#quantitative"
        exeWriLink = "../exercise/" + userID + "#writing"
        appLink = "../application/" + userID       
        return render_to_response('stu/exercise.html', locals())
    return render(request, 'stu/exercise.html')

@csrf_exempt
def exams(request, userID):
    if request.method == "GET":
        examObject = StuExam.objects.all()
        examCityitem = set()
        for obj in examObject:
            examCityitem.add(obj.as_dict()['examcity'])
        examCityitem = sorted(list(examCityitem))

        examitems = [obj.as_dict() for obj in examObject]
        examJson = json.dumps(examitems)

        stu = Student.objects.get(stu_id=userID)
        name = stu.stu_fname + stu.stu_lname
        proLink = "../profile/" + userID
        enrollLink = "../enrollment/" + userID
        exeLink = "../exercise/" + userID
        exeVerLink = "../exercise/" + userID + "#verbal"
        exeQuaLink = "../exercise/" + userID + "#quantitative"
        exeWriLink = "../exercise/" + userID + "#writing"
        appLink = "../application/" + userID      
        return render_to_response('stu/tables-exams.html', locals())

    if request.method == "POST":
        appliedExamID = request.POST.get("appliedExamID")
        AppliedExam.objects.create(stu_id=userID, exam_id=appliedExamID)
        examObject = StuExam.objects.get(exam_id=appliedExamID)
        examObject.availability = 0
        examObject.save(update_fields=['availability'])
        return redirect('/stu/profile/%s' %userID, locals())
    
    return render(request, 'stu/tables-exams.html')

def download(request):
    name = request.GET.get('name')
    file = open(name, 'rb')
    response = FileResponse(file)
    response['Content-Type']='application/msword'
    response['Content-Disposition']='attachment;filename='+name
    return response

@csrf_exempt
def upload_file(request, userID): 
    if request.method == "POST":
        resume = request.FILES.get("resume", None)
        transcript = request.FILES.get("transcript", None)
        recommendation = request.FILES.get("recommendation", None)
        stu_resume_name = ""
        transcript_name = ""
        recommendation_name = ""

        stu_app_id = "X" + time.strftime("%Y%m%d%H%M%S", time.localtime()) 
        status = "pending"

        if resume:
            stu_resume_name = "/root/upload/resume/resume/" + stu_app_id + "resume.pdf"
            destination = open(stu_resume_name,'wb+')
            for chunk in resume.chunks():       
                destination.write(chunk) 
            destination.close()
        if transcript:
            transcript_name = "/root/upload/resume/transcript/" + stu_app_id + "transcript.pdf"
            destination = open(transcript_name,'wb+')
            for chunk in transcript.chunks():       
                destination.write(chunk) 
            destination.close()
        if recommendation:
            recommendation_name = "/root/upload/resume/recommendation/" + stu_app_id + "recommendation.pdf"
            destination = open(recommendation_name,'wb+')
            for chunk in recommendation.chunks():       
                destination.write(chunk) 
            destination.close()
        
        accountType = request.POST.get("account")
        accountID = ""
        university = University.objects.all()
        for obj in university:
            if obj.uni_name == accountType:
                accountID = obj.uni_id
                break

        StuApplication.objects.create(stu_app_id=stu_app_id, stu_resume=stu_resume_name, transcript=transcript_name, recommendation=recommendation_name, stu_id=userID, apply_uni_id=accountID, status=status)
        
        return redirect('/stu/profile/%s' %userID, locals()) 
        # return render(request, 'stu/profile/%s' %userID, locals())