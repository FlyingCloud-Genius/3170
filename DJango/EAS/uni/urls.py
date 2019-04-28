from django.urls import path
from . import views

urlpatterns = [ 
    path('profile/<str:userEmail>', views.profile, name='university-profile'),
    path('infoEdition', views.infoEdition, name = 'university-edit')

]