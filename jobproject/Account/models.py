

from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
import datetime
from django_countries.fields import CountryField
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, email,username,contact,is_company,is_employee,password=None):
        
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        
            contact = contact,
            is_company=is_company,
            is_employee=is_employee,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user



    
    def create_superuser(self,username,password,email ):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            # first_name = first_name,
            # last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


 
class Account(AbstractBaseUser,PermissionsMixin):
    language_choices=(('English','English'),('Malayalam','Malayalam'),('Hindi','Hindi'))
    skill_choices=(('Django','Django'),('Html','Html'),('PHP','PHP'),('Java','Java'))
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


    id            = models.AutoField(primary_key=True)
    first_name      = models.CharField(max_length=50, default='')
    last_name       = models.CharField(max_length=50, default='')
   
    username        = models.CharField(max_length=50, unique=True)
    email           = models.EmailField(max_length=100, unique=True)
    contact         = models.BigIntegerField(default=0)
    address =        models.CharField(max_length=150,default='')
    country          = CountryField(max_length=50,blank_label='(select country)')
    gender          = models.CharField(max_length=50, default='None')
    # dob             =models.DateField(default=datetime.date.today())
    dob             =models.CharField(max_length=50,default='')
    language=models.CharField(max_length=50,choices=language_choices,default='')
    skills=models.CharField(max_length=50,choices=skill_choices,default='')
    state           = models.CharField(max_length=50,choices=state_choices,default='')
    district        = models.CharField(max_length=50,choices=district_choices,default='')

    profilepic         = models.ImageField(upload_to="Profile",blank=True, null=True)
    Resume         = models.FileField(upload_to="Resume",blank=True, null=True)



    # required
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_company      = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_superadmin   = models.BooleanField(default=False)
    is_employee       = models.BooleanField(default=False)   
    is_staff        = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username', 'first_name', 'last_name','district','state','gender','contact']
    REQUIRED_FIELDS = ['username','password']




    objects = MyAccountManager()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

class JobDetails(models.Model):
    id  = models.AutoField(primary_key=True)
    email= models.ForeignKey(Account,null=True,blank=True, on_delete=models.CASCADE)
    jobname=models.CharField(max_length=250,default='')
    companyname=models.CharField(max_length=250,default='')
    jobtype=models.CharField(max_length=250,default='')
    companyaddress=models.CharField(max_length=250,default='')
    jobdescription=models.TextField(max_length=1500,default='')
    qualification=models.TextField(max_length=1500,default='')
    responsibility=models.TextField(max_length=1500,default='')
    location=models.CharField(max_length=250,default='')
    companywebsite=models.CharField(default='',max_length=20)
    companycontact=models.BigIntegerField(default=0)
    companyemail=models.EmailField(max_length=50,default='')
    salarypackage=models.CharField(max_length=40,default='')
    experience=models.CharField(max_length=40,default='')
    logo=models.ImageField(upload_to="logos",default='')


class Applylist(models.Model):
   cand=models.ForeignKey(Account,on_delete=models.CASCADE)
   job=models.ForeignKey(JobDetails,on_delete=models.CASCADE)
   education=models.CharField(max_length=200,default='')
   minsalary=models.CharField(max_length=20,default='')
   maxsalary=models.CharField(max_length=20,default='')
   resume=models.FileField(upload_to="resume")