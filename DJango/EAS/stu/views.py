from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
from .models import Student, StuPhones

def profile(request):
    if request.method == "GET":
        stu = Student.objects.get(stu_email = "133228573@qq.com")
        # print("gender: ")
        # print(stu.stu_gender)
        if stu.stu_gender == 0:
            gender = "Male"
        return render_to_response('stu/personal-profile.html', locals())
        #render(request, 'stu/personal-profile.html') #, {'gender': gender}

    return HttpResponse(request)


def application(request):
    pass
    return render(request, 'stu/application.html')


def exercise(request):
    pass
    return render(request, 'stu/exercise.html')


def exams(request):
    pass
    return render(request, 'stu/tables-exams.html')


def grades(request):
    pass
    return render(request, 'stu/tables-grades.html')