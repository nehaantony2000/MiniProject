
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
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



    
    def create_superuser(self,username,password,email,**extra_fields):
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


 
class Account(AbstractBaseUser):
    


    id            = models.AutoField(primary_key=True)
    first_name      = models.CharField(max_length=50, default='')
    last_name       = models.CharField(max_length=50, default='')
   
    username        = models.CharField(max_length=50, unique=True)
    email           = models.EmailField(max_length=100, unique=True)
    contact         = models.BigIntegerField(default=0)
    country          = CountryField(max_length=50,blank_label='(select country)')
    gender          = models.CharField(max_length=50, default='None')
    dob             =models.DateField(default=datetime.date.today())

    usr_img         = models.ImageField(upload_to="images/",blank=True, null=True)


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