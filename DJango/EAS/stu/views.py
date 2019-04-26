from django.shortcuts import render


# Create your views here.
def profile(request):
    pass
    return render(request, 'stu/personal-profile.html')


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