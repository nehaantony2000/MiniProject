from django.db import models
from Account.models import Account
from django_countries.fields import CountryField
# Create your models here.
class Company(models.Model):
    
   id = models.AutoField(primary_key=True)
   email = models.ForeignKey(Account, on_delete=models.CASCADE)
   company_name= models.CharField(max_length=50)
   address = models.CharField(max_length=150)
   logo         = models.ImageField(upload_to="images/Company/",blank=True, null=True)
   

class Job(models.Model):

    image=models.ImageField(upload_to='pics')
    title=models.CharField(max_length=250)
    location=models.CharField(max_length=200)
    desp=models.TextField()
    companyname=models.CharField(max_length=250)