from django.urls import path

from . import views

urlpatterns = [ 
    path('profile', views.profile, name='personal-profile'),
    path('application', views.profile, name='personal-profile'),

]