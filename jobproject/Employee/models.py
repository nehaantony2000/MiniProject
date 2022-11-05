import datetime
from unittest.util import _MAX_LENGTH
from django.db import models
from Account.models import Account
from django_countries.fields import CountryField
# Create your models here.

    
class Employee (models.Model):
    
   state_choices = (('kerala','kerala'),('demo','demo'),('None','None'))
   gender_choices=(('Male','Male'),('Female','Female'),('others','others'), ('None','None'))
   district_choices=(
        ('Kozhikode','Kozhikode'),
        ('Malappuram','Malappuram'),
        ('Kannur','Kannur'),
        ('Trivandrum','Trivandrum'),
        ('Palakkad','Palakkad'),
        ('Thrissur','Thrissur'),
        ('Kottayam','Kottayam'),
        ('Alappuzha','Alappuzha'),
        ('Idukki','Idukki'),
        ('Kollam','Kollam'),
        ('Ernakulam','Ernakulam'),
        ('Wayanad','Wayanad'),
        ('Kasaragod','Kasaragod'),
        ('Pathanamthitta','Pathanamthitta'),
        ('Thiruvananthapuram','Thiruvananthapuram'),
        ('None','None'),
    )
   id = models.AutoField(primary_key=True)
   email =          models.ForeignKey(Account, on_delete=models.CASCADE)
   country          = CountryField(max_length=50,blank_label='(select country)')
   gender          = models.CharField(max_length=50, default='None')
   dob             =models.CharField(max_length=50)
   state           = models.CharField(max_length=50,choices=state_choices,default='kerala')
   district        = models.CharField(max_length=50,choices=district_choices,default='None')
   city= models.CharField(max_length=50)
   address = models.CharField(max_length=150)
   profile_pic         = models.ImageField(upload_to="images/Candidate/",blank=True, null=True)
   Resume         = models.FileField(upload_to="Files/",blank=True, null=True)



class Joblist(models.Model):

    image=models.ImageField(upload_to='pics')
    title=models.CharField(max_length=250)
    location=models.CharField(max_length=200)
    desp=models.TextField()
    companyname=models.CharField(max_length=250)