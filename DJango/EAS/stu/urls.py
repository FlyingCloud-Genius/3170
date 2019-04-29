from django.urls import path

from . import views

urlpatterns = [ 
    path('editor/<str:userID>', views.editor, name='personal-edit'),
    path('profile/<str:userID>', views.profile, name='personal-profile'),
    path('profile/download/', views.download, name='pro-download'),
    path('profile/uploadfile/<str:userID>', views.upload_file, name="uploadfile"),
    path('application/<str:userID>', views.application, name='application'),
    path('exercise/<str:userID>', views.exercise, name='exercise'),
    path('exercise/download/', views.download, name='exer-download'),
    path('enrollment/<str:userID>', views.exams, name='tables-exams')
]