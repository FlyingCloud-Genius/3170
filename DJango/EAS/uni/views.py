from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse

from .models import University, UniOpenMajor
# Create your views here.
def profile(request):
    if request.method == "GET":
        uni = University.objects.get(uni_email = "admissions@cuhk.edu.cn")
        #get university info
        name = uni.uni_name
        phone = uni.uni_phone
        email = uni.uni_email
        web = uni.uni_web
        # photo

        #get student application
        
        return render_to_response('uni/university-profile.html', locals())
    return HttpResponse(request)