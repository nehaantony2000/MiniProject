from django.urls import path
from . import views


urlpatterns = [

  
    path ('login/', views.login, name="login"),
    path ('register/', views.register, name="register"),
    path('logout/', views.logout, name="logout"),
    path('Company_Changepass/', views.comp_change_password, name='Company_Changepass'),
    path('Change_Password/', views.change_password, name='change_password'),
     path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
     path('activate/<uidb64>/<token>/', views.activate, name='activate'),


    ]