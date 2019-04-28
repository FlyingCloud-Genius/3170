from django.urls import path

from . import views

urlpatterns = [ 
    path('profile', views.profile, name='university-profile'),
    path('infoChange', views.infoChange, name = 'university-profile')

]