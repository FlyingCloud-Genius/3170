from django.urls import path

from . import views

urlpatterns = [ 
    path('editor/<str:userID>', views.editor, name='guardian-edit'),
    path('profile/<str:userID>', views.profile, name='guardian-profile'),
    path('exams/<str:userID>', views.exams, name='tables-exams-guard'),
    path('exercises/<str:userID>', views.exercises, name='tables-exercises-guard'),
    path('grades/<str:userID>', views.grades, name='tables-grades-guard'),
]