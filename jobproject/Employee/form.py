from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Employee
from Account.models import Account

class UserForm(forms.ModelForm):
    class Meta:
        model=Account
        # exclude=['']
        fields=['first_name','last_name','country','contact','usr_img','dob','gender']

        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'country':forms.Select(attrs={'class':'form-control','placeholder':'Country'}),
            # 'state':forms.Select(attrs={'class':'form-control','placeholder':'State'}),
            # 'district':forms.Select(attrs={'class':'form-control','placeholder':'District'}),
            'contact':forms.NumberInput(attrs={'class':'form-control','placeholder':'Contact'}),
            'usr_img':forms.FileInput(attrs={'class':'form-control','placeholder':'Image'}),

            # 'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            # 'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
            # 'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'dob':forms.DateInput(attrs={'class':'form-control','placeholder':'Date of Birth'}),
            'gender':forms.Select(attrs={'class':'form-control','placeholder':'Enter Gender'}),
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['job_title','experience','Company_name','SSLC','SSLC_percentage','High_school','HighSchool_percentage','UG','UG_percentage','PG','PG_percentage']
        widgets={
            'job_title':forms.Select(attrs={'class':'form-control','placeholder':'specialization'}),
            'experience':forms.NumberInput(attrs={'class':'form-control','placeholder':'Experience'}),
            'Company_name':forms.SelectMultiple(attrs={'class':'form-control','placeholder':'Company Name'}),
            # 'license_no':forms.TextInput(attrs={'class':'form-control','placeholder':'License No'}),
            # 'des_name':forms.Select(attrs={'class':'form-control','placeholder':'Designation'}),
            'SSLC':forms.Select(attrs={'class':'form-control','placeholder':'SSLC'}),
            'SSLC_percentage':forms.NumberInput(attrs={'class':'form-control','placeholder':'Percentage'}),
            'High_school':forms.Select(attrs={'class':'form-control','placeholder':'High School'}),
            'HighSchool_percentage':forms.NumberInput(attrs={'class':'form-control','placeholder':' Percentage'}),
            'UG':forms.Select(attrs={'class':'form-control','placeholder':'Under Graduate'}),
            'UG_percentage':forms.NumberInput(attrs={'class':'form-control','placeholder':'Percentage'}),
            'PG':forms.Select(attrs={'class':'form-control','placeholder':'Post Graduate'}),
            'PG_percentage':forms.NumberInput(attrs={'class':'form-control','placeholder':'Percentage'}),
        }