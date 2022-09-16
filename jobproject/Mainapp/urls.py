from django.urls import path
from . import views


urlpatterns = [

    path ('',views.index),
    path('Userhome/',views.userhome),
    path('Adminhome/',views.adminhome),
    path('Companyhome/',views.companyhome),

    ]