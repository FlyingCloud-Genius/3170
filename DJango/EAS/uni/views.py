from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from reg.models import RegInfo
from django.views.decorators.csrf import csrf_exempt
from .models import University, UniOpenMajor

# Create your views here.
@csrf_exempt
def profile(request, userEmail):
    if request.method == "GET":
        uni = University.objects.get(uni_email = userEmail)

        #get university info
        name = uni.uni_name
        phone = uni.uni_phone
        email = uni.uni_email
        web = uni.uni_web
        # photo

        #get student application
        
        return render_to_response('uni/university-profile.html', locals())

    elif request.method == "POST":
        print ("helpless")
        return redirect('../editorCreate/%s' %userEmail)
    return HttpResponse(request)

def editorCreate(request, userEmail):
    if request.method == "GET":
        return render(request, "uni/university-edit.html")
    return render_to_response('uni/university-edit.html', locals())


def infoEdition(request, userEmail):
    if request.method == "POST":
        uni = University.objects.get(uni_email = userEmail)
        if request.POST.get('password') != request.POST.get('reppassword'):
            message = "the passwords has to be the same!!"
            return render_to_response('uni/university-edit.html', {"message": message})
        uni.uni_name = request.POST.get('username')
        uni.uni_phone = request.POST.get('contactNum')
        uni.uni_web = request.POST.get('officialWebsite')
        uni.required_score = request.POST.get('requirement')
        
        regInfo = RegInfo.objects.get(reg_id = uni.reg)
        regInfo.password = request.POST.get('password')
        regInfo.save()
        uni.save()
    return redirect(request, 'profile/%s' %userEmail) 