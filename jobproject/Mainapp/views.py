
from django.shortcuts import render
from Account.models import Account,JobDetails,Applylist



def index(request):
    Job=JobDetails.objects.all()
    for i in Job:
      
     context={
        'job_list':Job
    }
    return render(request,'index.html',context)

def contact(request):
    
    return render(request,'contact.html')



