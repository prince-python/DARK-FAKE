from django.urls import path,include
from .import views





urlpatterns = [
    path('',views.index),
    path('ccsearch/',views.ccsearch),
    path('profile/',views.profile),
    path('fprofile/',views.fprofile),
    path('mail/',views.mail),
    path('fmail/',views.fmail),
    
]
