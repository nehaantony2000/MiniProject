from django.urls import path
from . import views


urlpatterns = [


    
    path ('Companyhome/', views.Companyhome, name="Companyhome"),
    path ('postjob/', views.postjob, name="postjob"),
    path ('C_profile/', views.company_profile, name="C_profile"),
]