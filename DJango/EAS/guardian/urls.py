from django.urls import path

from . import views

urlpatterns = [ 
    path('editor/<str:userID>', views.editor, name='guardian-edit'),
    path('profile/<str:userID>', views.profile, name='guardian-profile'),
    path('exams', views.exams, name='tables-exams-guard'),
    path('exercises', views.exercises, name='tables-exercises-guard'),
    path('grades', views.grades, name='tables-grades-guard'),
]