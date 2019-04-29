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
        profileLink = "uni/university-profile/" + userEmail
        
        return render_to_response('uni/university-profile.html', locals())

    elif request.method == "POST":
        print ("helpless")
        return redirect('../editorCreate/%s' %userEmail)
    return HttpResponse(request)

@csrf_exempt
def editorCreate(request, userEmail):
    print(request.GET.get('username'))
    print(request.GET.get('contactNum'))
    print(request.GET.get('officialWebsite'))
    print(request.GET.get('requirement'))

    if request.method == "GET":
        print ("fuck")
        return render(request, "uni/university-edit.html")
    elif request.method == "POST" and request.POST:
        if request.POST.get('username') == request.POST.get('contactNum') == request.POST.get('officialWebsite') == request.POST.get('requirement') != None:
            return redirect("../profile/%s" %userEmail)

        uni = University.objects.get(uni_email = userEmail)
        uni.uni_name = request.POST.get('username')
        uni.uni_phone = request.POST.get('contactNum')
        uni.uni_web = request.POST.get('officialWebsite')
        uni.required_score = request.POST.get('requirement')
        uni.save()
        return redirect('../profile/%s' %userEmail) 
    return render_to_response('uni/university-edit.html', locals())

