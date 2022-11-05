from django.shortcuts import render
from .models import Company,Job
from Account.models import Account


def Companyhome(request):
    return render(request,'Company/CompanyHome.html')

def postjob(request):
    return render(request,'Company/JobPost.html')
def company_profile(request):

      email = request.session.get('email')
         
      usr=Account.objects.filter(email=email)
            
      print(usr)
           
      comp=Company.objects.filter(email__email=usr)
      context = {
                'company': comp,
                'usr':usr,
                
            }
      return render(request, 'Company/Company_profile.html', context)