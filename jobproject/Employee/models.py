
from django.db import models
from datetime import date
from Account.models import Account
from django import forms
from django.utils import timezone
# Create your models here.

JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.ForeignKey(Account, on_delete=models.CASCADE)
   
    is_employee = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    
    job_title = models.CharField(max_length=300)
    description = models.TextField()
    Company_name = models.CharField(max_length=300)
    address = models.CharField(max_length=150)
    type = models.CharField(choices=JOB_TYPE, max_length=10)
    # category = models.CharField(max_length=100)
    last_date = models.DateTimeField()
    SSLC =models.CharField(max_length=150)
    SSLC_percentage=models.IntegerField()
    High_school =models.CharField(max_length=150)
    HighSchool_percentage=models.IntegerField()
    UG =models.CharField(max_length=150)
    UG_percentage=models.IntegerField()
    PG =models.CharField(max_length=150)
    PG_percentage=models.IntegerField()

    experience = models.IntegerField(blank=False, null=False)
    # license_no = models.CharField(max_length=100, blank=True)
    # company_name = models.CharField(max_length=100)
    # company_description = models.CharField(max_length=300)
    # website = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(default=timezone.now)
    filled = models.BooleanField(default=False)

    def __str__(self):
        return self.job_title

