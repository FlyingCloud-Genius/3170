from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from .models import Guardian
from stu.models import StuExam, StuExercise, StuAnswerSheet, AppliedExam
import json, os

@csrf_exempt
def profile(request, userID):
    if request.method == "GET":
        appliedExam =  list(AppliedExam.objects.values_list('stu_id', 'exam_id'))
        examitems = []
        examObject = StuExam.objects.all()
        for obj in appliedExam:
            if obj[0] == userID:
                for dd in examObject:
                    if dd.exam_id == obj[1]:
                        examitems += [dd.as_dict()]

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
        return redirect('/guardian/editor/%s' %userID)
    else:
        return render(request, 'guardian/guardian-profile.html')

@csrf_exempt
def editor(request, userID):
    if request.method == "POST":
        message = "You should agree with the privacy of Exam and Application System"
        check_box = request.POST.getlist('check_box')
        if check_box: 
            print(userID)       
            guardian = Guardian.objects.get(guardian_id=userID)
            if ((request.POST.get('firstName') == "" and guardian.guardian_fname == None) or (request.POST.get('lastName') == ""  and guardian.guardian_lname == None)):
                message = "Your name must be filled !"
                return render(request, 'guardian/guardian-edit.html', {"message": message})
            else:
                if request.POST.get('firstName') != "":
                    guardian.guardian_fname = request.POST.get('firstName')
                if request.POST.get('lastName') != "":    
                    guardian.guardian_lname = request.POST.get('lastName')
                if request.POST.get('phoneNum') != "":    
                    guardian.guardian_phone = request.POST.get('phoneNum')   
                guardian.save()
                return redirect('/guardian/profile/%s' %userID) 
        return render(request, 'guardian/guardian-edit.html', {"message": message}) 
    return render(request, 'guardian/guardian-edit.html')

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

        guardian = Guardian.objects.get(guardian_id=userID)
        name = guardian.guardian_fname + guardian.guardian_lname
        ProfileLink = "../profile/" + userID
        ExercisesLink = "../exercises/" + userID
        GradesLink = "../grades/" + userID
        ExamsLink = "../exams/" + userID
        return render_to_response('guardian/tables-exams-guard.html', locals())

    if request.method == "POST":
        appliedExamID = request.POST.get("appliedExamID")
        AppliedExam.objects.create(stu_id=userID, exam_id=appliedExamID)
        return redirect('/guardian/profile/%s' %userID, locals())

    return render(request, 'guardian/tables-exams-guard.html')

@csrf_exempt
def exercises(request, userID):
    if request.method == "GET":
        guardian = Guardian.objects.get(guardian_id=userID)
        exerciseObject = StuExercise.objects.all()
        exerciseItem = [obj.as_dict() for obj in exerciseObject]
        exerciseJson = json.dumps(exerciseItem)

        name = guardian.guardian_fname + guardian.guardian_lname
        ProfileLink = "../profile/" + userID
        ExercisesLink = "../exercises/" + userID
        GradesLink = "../grades/" + userID
        ExamsLink = "../exams/" + userID
        uploadURL = "../exercises/uploadfile/" + userID
        return render_to_response('guardian/tables-exercises-guard.html', locals())
    return render(request, 'guardian/tables-exercises-guard.html')

@csrf_exempt
def grades(request, userID):
    if request.method == "GET":
        ansSheetObject = StuAnswerSheet.objects.all()
        ansSheetItem = [obj.as_dict() for obj in ansSheetObject]
        ansSheetJson = json.dumps(ansSheetItem)

        guardian = Guardian.objects.get(guardian_id=userID)
        name = guardian.guardian_fname + guardian.guardian_lname
        ProfileLink = "../profile/" + userID
        ExercisesLink = "../exercises/" + userID
        GradesLink = "../grades/" + userID
        ExamsLink = "../exams/" + userID
        commitURL = "../grades/commit/" + userID
        return render_to_response('guardian/tables-grades-guard.html', locals())
    return render(request, 'guardian/tables-grades-guard.html')

@csrf_exempt
def upload_file(request, userID):
    if request.method == "POST":
        newContent = request.FILES.get("newContent", None)
        newAnswer = request.FILES.get("newAnswer", None)
        newAnalysis = request.FILES.get("newAnalysis", None)
        newID = request.POST.get("newID", None)
        newType = request.POST.get("newType", None)
        newLevel = request.POST.get("newLevel", None)
        content_name = ""
        answer_name = ""
        analysis_name = ""
        
        if newID:
            exerciseObject = StuExercise.objects.all()
            for item in exerciseObject:
                if item.que_id == newID:
                    item.que_type = newType
                    if newContent:
                        content_name = "/root/upload/exercise/" + newID + "content.pdf"
                        destination = open(content_name,'wb+')
                        for chunk in newContent.chunks():       
                            destination.write(chunk) 
                        destination.close()
                        item.que_content=content_name
                    if newAnswer:
                        answer_name = "/root/upload/exercise/" + newID + "answer.pdf"
                        destination = open(answer_name,'wb+')
                        for chunk in newAnswer.chunks():       
                            destination.write(chunk) 
                        destination.close()
                        item.answer=answer_name
                    if newAnalysis:
                        analysis_name = "/root/upload/exercise/" + newID + "analysis.pdf"
                        destination = open(analysis_name,'wb+')
                        for chunk in newAnalysis.chunks():       
                            destination.write(chunk) 
                        destination.close()
                        item.que_analysis=analysis_name
                    item.save()
                    return redirect('/guardian/exercises/%s' %userID, locals())

            if newContent:
                content_name = "/root/upload/exercise/" + newID + "content.pdf"
                destination = open(content_name,'wb+')
                for chunk in newContent.chunks():       
                    destination.write(chunk) 
                destination.close()
            if newAnswer:
                answer_name = "/root/upload/exercise/" + newID + "answer.pdf"
                destination = open(answer_name,'wb+')
                for chunk in newAnswer.chunks():       
                    destination.write(chunk) 
                destination.close()
            if newAnalysis:
                analysis_name = "/root/upload/exercise/" + newID + "analysis.pdf"
                destination = open(analysis_name,'wb+')
                for chunk in newAnalysis.chunks():       
                    destination.write(chunk) 
                destination.close()
            
            StuExercise.objects.create(que_id=newID, que_type=newType, que_analysis=analysis_name, difficulty_level=newLevel, que_content=content_name, answer=answer_name)
            return redirect('/guardian/exercises/%s' %userID, locals())

        return redirect('/guardian/exercises/%s' %userID, locals())

@csrf_exempt
def commit(request, userID):
    if request.method == "POST":
        newGrade = request.POST.get("newGrade")
        appID = request.POST.get("ansID")
        aso = StuAnswerSheet.objects.get(ans_id=appID)
        if newGrade:
            aso.ans_score = newGrade
        aso.save()
        return redirect('/guardian/grades/%s' %userID, locals()) 

def download(request):
    name = request.GET.get('name')
    file = open(name, 'rb')
    response = FileResponse(file)
    response['Content-Type']='application/msword'
    response['Content-Disposition']='attachment;filename='+name
    return response