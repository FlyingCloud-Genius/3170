from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse


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

def getApplications(request, cur_email):
    if request.method == "GET":
        return
    return