from django.urls import path
from . import views


urlpatterns = [
    path('r/', views.dashboard, name="r"),
    path('createcv/', views.createCv, name="createcv"),
    path('skill-save/', views.saveSkill, name="skill-save"),
    path('edu-save/', views.saveEducation, name="edu-save"),
    path('ref-save/', views.saveReferee, name="ref-save"),
    path('profile-save/', views.uploadProfile, name="profile-save"),
    path('cv-detail/<id>', views.viewPDF, name="cv-detail"),
    path('cv-download/<id>', views.generate_PDF, name="cv-download"),
    path('cv-edit/', views.editCv, name="cv-edit"),
    path('cv-edit/fetchprofile/', views.fetchProfile, name="fetchprofile"),
    path('cv-edit/updateprofile/', views.updateProfile, name="profile-update"),
    path('cv-edit/deleteprofile/', views.deleteProfile, name="profile-delete"),
    path('cv-edit/eduview/', views.educationView, name="edu-view"),
    path('cv-edit/eduview/academic/', views.fetchAcademic, name="fetchacademic"),
    path('cv-edit/eduview/update_academic/', views.updateAcademic, name="update_academic"),
    path('cv-edit/eduview/delete_academic/', views.deleteAcademic, name="delete_academic"),
    ]