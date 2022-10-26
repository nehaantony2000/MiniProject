from django.urls import path
from . import views


urlpatterns = [

    path ('',views.index),
    path('Adminhome/',views.adminhome),
    path('Companyhome/',views.companyhome),

    ]