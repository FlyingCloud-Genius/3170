from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from reg.models import RegInfo
from django.views.decorators.csrf import csrf_exempt
from .models import University, UniOpenMajor
from stu.models import StuApplication
from django.contrib import messages
import json
# Create your views here.

@csrf_exempt
def profile(request, userEmail):
    if request.method == "GET":
        applications = StuApplication.objects.all()
        uni = University.objects.get(uni_email = userEmail)
        appItem = []
        for app in applications:
            if app.apply_uni_id == uni.uni_id:
                appItem += [app.as_dict()]
        appJson = json.dumps(appItem)
        
        name = uni.uni_name
        phone = uni.uni_phone
        email = uni.uni_email
        web = uni.uni_web
        profileLink = "uni/university-profile/" + userEmail
        agreeURL = "../profile/agree/" + userEmail
        return render_to_response('uni/university-profile.html', locals())

    elif request.method == "POST":
        return redirect('../editorCreate/%s' %userEmail)
    return HttpResponse(request)

@csrf_exempt
def editorCreate(request, userEmail):
    if request.method == "GET":
        return render(request, "uni/university-edit.html")
    elif request.method == "POST" and request.POST:
        message = "You should agree with the privacy of Exam and Application System"
        check_box = request.POST.getlist('check_box')
        if check_box: 
            uni = University.objects.get(uni_email = userEmail)
            if request.POST.get('username') == "" and uni.uni_name == None:
                message = "University name must be filled !"
                return render(request, 'uni/university-edit.html', {"message": message})
            else:
                if request.POST.get('username') != "":
                    uni.uni_name = request.POST.get('username')
                if request.POST.get('contactNum') != "":    
                    uni.uni_phone = request.POST.get('contactNum')
                if request.POST.get('officialWebsite') != "":    
                    uni.uni_web = request.POST.get('officialWebsite')
                if request.POST.get('requirement') != "":     
                    uni.required_score = request.POST.get('requirement')
                uni.save()
                return redirect('../profile/%s' %userEmail) 
        else:
            return render(request, 'uni/university-edit.html', {"message": message})
    return render(request, "uni/university-edit.html")


@csrf_exempt
def agree(request, userEmail):
    if request.method == "POST":
        newStatus = request.POST.get('account')
        thisAppID =request.POST.get('appliedID')
        sao = StuApplication.objects.get(stu_app_id=thisAppID)
        if newStatus == "Pass":
            sao.status = "Pass"
        elif newStatus == "Reject":
            sao.status = "Reject"
        sao.save()
        return redirect('/uni/profile/%s' %userEmail, locals()) 

def download(request):
    name = request.GET.get('name')
    file = open(name, 'rb')
    response = FileResponse(file)
    response['Content-Type']='application/msword'
    response['Content-Disposition']='attachment;filename='+name
    return response