from django.shortcuts import render,redirect
from .models import Employee,Joblist
from Account.models import Account
from django.db.models import Q
from django.contrib import messages
def employee_profile(request):
    if request.user.is_authenticated:
      email = request.session.get('email')
         
      usr=Account.objects.filter(email=email)
            
      emp=Employee.objects.filter(email_id__email=usr)
      
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

def searchbar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            multiple_q = Q(Q(title__icontains=query) | Q(companyname__icontains=query))
            J= Joblist.objects.filter(multiple_q) 
            return render(request, 'searchbar.html', {'key1':J})
        else:
            messages.info(request, 'No search result!!!')
            print("No information to show")
    return render(request, 'searchbar.html', {}) 




