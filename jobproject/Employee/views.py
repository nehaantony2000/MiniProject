from django.shortcuts import render,redirect
from .models import Employee,Joblist
from Account.models import Account

def employee_profile(request):

      email = request.session.get('email')
         
      usr=Account.objects.filter(email=email)
            
      print(usr)
           
      emp=Employee.objects.filter(email__email=usr)
      context = {
                'employee': emp,
                'usr':usr,
                
            }
      return render(request, 'Employee/Employee_profile.html', context)
 
            

def joblist(request):
    J=Joblist.objects.all()
    return render(request,'Employee/joblist.html',{'key1':J})
      
            
        

def Update_profile(request):
    usr=Account.objects.get(email=request.session.get('email'))
    emp=Employee.objects.get(email__id=Account.objects.get(email=request.session.get('email')).id)
       
     
# def joblist(request):
#     J=Joblist.objects.all()
#     return render(request,'Employee/joblist.html',{'key1':J})

def topcompany(request):
    # J=Joblist.objects.all()
    return render(request,'Company/Top_company.html')

def userhome(request):
     if request.user.is_authenticated:
        if request.user.is_employee:
            email = request.session.get('email')
            print(email)
            
    
     return render(request, 'Employee/userhome.html')