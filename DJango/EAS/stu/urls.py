from django.urls import path

from . import views

urlpatterns = [ 
    path('profile', views.profile, name='personal-profile'),
    path('application', views.application, name='application'),
    path('exercise', views.exercise, name='exercise'),
    path('enrollment', views.exams, name='tables-exams'),
    path('grades', views.grades, name='tables-grades'),

]