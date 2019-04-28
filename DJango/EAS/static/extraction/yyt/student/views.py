from django.shortcuts import render

# Create your views here.

def getData(request):
    if request.method == "GET":
        gender = request.GET.get("gender")
        phone = request.GET.get("phone")
        email = request.GET.get("email")
        uni = request.GET.get("university")
        major = request.GET.get("major")
        
    

    return render(request，'reg/profile.html')