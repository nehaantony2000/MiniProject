from django.urls import path
from . import views


urlpatterns = [

    path ('userhome/', views.userhome, name="userhome"),
    path ('E_profile/', views.employee_profile, name="E_profile"),
    path ('joblist/', views.joblist, name="joblist"),
    path ('Top_Company/', views.topcompany, name="topcompany"),
]