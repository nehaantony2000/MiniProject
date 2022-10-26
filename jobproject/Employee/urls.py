

from django.urls import path, include
from . import views

urlpatterns = [
    path('userhome/',views.userhome, name='userhome'),
    path('update/',views.EmployeeUpdate, name='EmployeeUpdate'),
     path('joblist/',views.Joblist, name='Joblist')
]