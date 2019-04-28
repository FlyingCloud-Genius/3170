from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from reg.models import RegInfo

from .models import University, UniOpenMajor
# Create your views here.
def profile(request, cur_email):
    if request.method == "GET":
        uni = University.objects.get(cur_email)

        #get university info
        name = uni.uni_name
        phone = uni.uni_phone
        email = uni.uni_email
        web = uni.uni_web
        # photo

        #get student application
        
        return render_to_response('uni/university-profile.html', locals())
    return HttpResponse(request)

def infoEdition(request, cur_email):
    if request.method == "POST":
        uni = University.objects.get(cur_email)
        if request.POST.get('password') != request.POST.get('reppassword'):
            message = "the passwords has to be the same!!"
            return render_to_response('uni/university-edit', {"message": message})
        uni.uni_name = request.POST.get('username')
        uni.uni_phone = request.POST.get('contactNum')
        uni.uni_web = request.POST.get('officialWebsite')
        uni.required_score = request.POST.get('requirement')
        
        regInfo = RegInfo.objects.get(uni.reg)
        regInfo.password = request.POST.get('password')
        regInfo.save()
        uni.save()
    return render(request, "uni/university-profile.html", locals())