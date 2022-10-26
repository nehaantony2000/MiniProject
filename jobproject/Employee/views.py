
import email
from operator import ge
from pydoc import doc
from django.shortcuts import render, redirect
from Account.models import Account
from .models import Employee
from datetime import date
from .form import EmployeeForm, UserForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def userhome(request):
    # if request.user.is_authenticated:
    #     if request.user.is_employee:
    #         email = request.session.get('email')
    #         print(email)

    #         usr=Account.objects.get(email=email)
    
    #         employee=Employee.objects.get(email__id=usr.id)
        
    
            
            # context = {
            #     'employee': employee,
            #     'usr':usr,
            #     'exp':date.today().year-employee.experience,
            # }
            
    
    return render(request, 'Employee/userhome.html')
    #     else:
    #         return redirect('login')
    # return redirect('login')
            

@login_required(login_url='login')
def EmployeeUpdate(request):
    usr=Account.objects.get(email=request.session.get('email'))
    employee=Employee.objects.get(email__id=Account.objects.get(email=request.session.get('email')).id)
    if request.method == 'GET':
        context={}
        context['usr_form']= UserForm(instance=Account.objects.get(email=request.session.get('email')))
        context['E_form']= EmployeeForm(instance=Employee.objects.get(email__id=Account.objects.get(email=request.session.get('email')).id))
        context['usr']=usr
        context['Employee']=employee
        return render(request, 'Employee/profile_update.html', context)
    else:
        form = UserForm(request.POST, request.FILES)
        employee = EmployeeForm(request.POST)
        # 
        if form.is_valid() and employee.is_valid():
            # email = request.session.get('email')
            usr=Account.objects.get(email=request.session.get('email'))
            usr.first_name = form.cleaned_data['first_name']
            usr.last_name = form.cleaned_data['last_name']
            # usr.state = form.cleaned_data['state']
            # usr.district = form.cleaned_data['district']
            usr.country = form.cleaned_data['country']
            usr.contact = form.cleaned_data['contact']
            usr.usr_img = form.cleaned_data['usr_img']
            usr.dob = form.cleaned_data['dob']
            print('inside')
            usr.save()
            E=Employee.objects.get(email__id=usr.id)
            E.job_title = employee.cleaned_data['job_title']
            E.experience = employee.cleaned_data['experience']
            E.SSLC = employee.cleaned_data['SSLC']
            E.SSLC_percentage = employee.cleaned_data['SSLC_percentage']
            E.High_School = employee.cleaned_data['High_School']
            E.HighSchool_percentage = employee.cleaned_data['HighSchool_percentage']
            E.UG = employee.cleaned_data['UG']
            E.UG_percentage = employee.cleaned_data['UG_percentage']
            E.PG = employee.cleaned_data['PG']
            E.PG_percentage = employee.cleaned_data['PG_percentage']
            E.des_name = employee.cleaned_data['des_name']
            print('inside2')
            E.save()
            return redirect('doctorHome')

        else:
            context={}
            context['form']= form
            context['employee']= employee
            context['usr']=usr
            context['employee']=employee
            return render(request, 'Employee/profile_update.html', context)



def Joblist(request):
    return render(request, 'Employee/joblist.html')