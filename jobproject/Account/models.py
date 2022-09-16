from django.db import models
from django.contrib.auth.models import User
 
class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    email=models.CharField(max_length=20)
    image = models.ImageField(upload_to="")
    gender = models.CharField(max_length=10)
    type = models.CharField(max_length=15)
 
    def __str__(self):
        return self.user.first_name
 
class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    image = models.ImageField(upload_to="")
    gender = models.CharField(max_length=10)
    type = models.CharField(max_length=15)
    status = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100)
 
    def __str__ (self):
        return self.user.username
