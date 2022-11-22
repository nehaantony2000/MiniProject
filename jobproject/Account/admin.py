
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account,JobDetails,Applylist
from django.contrib.auth.models import Group


admin.site.unregister(Group)
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','first_name', 'email','contact']
admin.site.register(Account, UserAdmin)


class UserAdmin(admin.ModelAdmin):
 list_display = ['jobname', 'companyname','companyaddress']
admin.site.register(JobDetails,UserAdmin)

class UserAdmin(admin.ModelAdmin):
 list_display = ['cand','job','maxsalary', 'education','minsalary']
admin.site.register(Applylist,UserAdmin)