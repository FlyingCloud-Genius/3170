from django.urls import path
from . import views

urlpatterns = [ 
    path('profile/<str:userEmail>', views.profile, name = 'university-profile'),
    path('editorCreate/<str:userEmail>', views.editorCreate, name = 'university-edit'),
    path('profile/agree/<str:userEmail>', views.agree, name="app-agree"),
    path('profile/download/<str:userEmail>', views.download, name='pro-download')
]