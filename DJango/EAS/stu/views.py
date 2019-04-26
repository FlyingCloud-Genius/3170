from django.shortcuts import render


# Create your views here.
def profile(request):
    print("I am in ./stu/profile")
    return render(request, 'stu/personal-profile.html')