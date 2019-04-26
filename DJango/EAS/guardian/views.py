from django.shortcuts import render

# Create your views here.
from .models import Guardian

def guardian(request):
    pass
    return render(request, 'guardian/guardian-profile.html')


def exams(request):
    pass
    return render(request, 'guardian/tables-exams-guard.html')


def exercises(request):
    pass
    return render(request, 'guardian/tables-exercises-guard.html')


def grades(request):
    pass
    return render(request, 'guardian/tables-grades-guard.html')