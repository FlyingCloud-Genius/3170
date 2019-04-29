from django.urls import path

from . import views

urlpatterns = [ 
    path('editor/<str:userID>', views.editor, name='guardian-edit'),
    path('profile/<str:userID>', views.profile, name='guardian-profile'),
    path('exams/<str:userID>', views.exams, name='tables-exams-guard'),
    path('exercises/<str:userID>', views.exercises, name='tables-exercises-guard'),
    path('exercises/download/', views.download, name='pro-download'),
    path('exercises/uploadfile/<str:userID>', views.upload_file, name="uploadfile"),
    path('grades/<str:userID>', views.grades, name='tables-grades-guard'),
    path('grades/download/', views.download, name='pro-download'),
    path('grades/commit/<str:userID>', views.commit, name="app-commit")
]