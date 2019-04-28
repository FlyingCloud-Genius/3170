from django.urls import path
from . import views

urlpatterns = [ 
    path('profile/<str:userEmail>', views.profile, name = 'university-profile'),
    path('infoEdition/<str:userEmail>', views.infoEdition, name = 'university-edit'),
    path('editorCreate/<str:userEmail>', views.editorCreate, name = 'university-edit')

]