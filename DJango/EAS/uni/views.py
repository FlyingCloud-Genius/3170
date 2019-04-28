from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse

from .models import University, UniOpenMajor
# Create your views here.
def profile(request):
    if request.method == "GET" and request.GET:
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

def infoChange(request):
    if request == "POST" and request.POST:
        uni_name = request.POST.get("username")
        uni_phone = request.POST.get("contactNum")
        uni_web = request.POST.get("officialWebsite")
        uni_score = request.POST.get("requirement")
        uni = University.objects.get(uni_email = )
        uni.uni_name = uni_name
        uni.uni_web = uni_web
        uni.uni_phone = uni_phone
        uni.required_gre_score = uni_score
        uni.save() #changes saved
        result = "success"
    return render(request, "templates/uni/university-profile.html", {"result": result})