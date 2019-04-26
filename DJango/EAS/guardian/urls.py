from django.urls import path

from . import views

urlpatterns = [ 
    path('profile', views.guardian, name='guardian-profile'),
    path('exams', views.exams, name='tables-exams-guard'),
    path('exercises', views.exercises, name='tables-exercises-guard'),
    path('grades', views.grades, name='tables-grades-guard'),
]