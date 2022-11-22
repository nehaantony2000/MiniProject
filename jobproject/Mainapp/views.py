
from django.shortcuts import render
from Account.models import Account,JobDetails,Applylist



def index(request):
    Job=JobDetails.objects.all()
    for i in Job:
      
     context={
        'job_list':Job
    }
    return render(request,'index.html',context)


def adminhome (request):
        return render(request,'Adminhome.html')
def companyhome (request):
        return render(request,'CompanyHome.html')
