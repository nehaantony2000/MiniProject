from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Account.models import Account,JobDetails,Applylist
from django.db.models import Q
from django.contrib import messages
from django.contrib import messages, auth

def profile(request):
    return render(request, 'Employee/Employee_profile.html')
 
def cat(request):
    return render(request,'Employee/category.html')

        
@login_required
def joblist(request):
    Job=JobDetails.objects.all()
    for i in Job:
      
     context={
        'job_list':Job
    }
    return render(request,'Employee/joblist.html',context)

@login_required(login_url='login')
def singlejob(request, id):
    Job=JobDetails.objects.filter(id=id)
    Job11=JobDetails.objects.get(id=id)

    context={
        'Job':Job,
       
    }
    return render(request,'Employee/singlejob.html',context)  
            
def Update_profile(request):
   if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact = request.POST.get('mobile')
        address = request.POST.get('address')
        country = request.POST.get('country')
        state = request.POST.get('state')
        dob = request.POST.get('dob')
        district=request.POST.get('District')
        gender = request.POST.get('gender')
        profilepic=request.FILES.get('pic')
        # skills=request.POST.get('skills')
        # languages=request.POST.get('languages')
        # education = request.POST.get('education')
        user_id = request.user.id
        
        user = Account.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.dob=dob
        user.profilepic=profilepic
        user.gender=gender
        user.contact = contact
        user.address = address
        user.district=district
        user.country=country
        user.state=state
        user.save()
        messages.success(request,'Profile Are Successfully Updated. ')
        return redirect('Eprofile')

          


        
        
        

     
# def joblist(request):
#     J=Joblist.objects.all()
#     return render(request,'Employee/joblist.html',{'key1':J})



def userhome(request):
    Job=JobDetails.objects.all()
    for i in Job:
      
     context={
        'job_list':Job
    }
     if request.user.is_authenticated:
       
        if request.user.is_employee:
            email = request.session.get('email')
    
 
     return render(request, 'Employee/userhome.html',context)

def searchbar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            multiple_q = Q(Q(jobname__icontains=query) | Q(companyname__icontains=query))
            J=JobDetails.objects.filter(multiple_q) 
            return render(request, 'searchbar.html', {'key1':J})
        else:
            messages.info(request, 'No search result!!!')
            print("No information to show")
    return render(request, 'searchbar.html', {}) 


@login_required
def Apply(request,pk):
    user=Account.objects.get(email=request.session.get('email'))
    if request.user.is_employee:
        job=JobDetails.objects.get(id=pk)
    return render(request, 'Employee/Applyjob.html',{'user':user,'job':job}) 

    
def ApplyJob(request,id):
   user=Account.objects.get(email=request.session.get('email'))
   if request.user.is_employee:
    job=JobDetails.objects.get(id=id)
    education=request.POST.get('edu')
    minsalary=request.POST.get('min')
    maxsalary=request.POST.get('max')
    resume=request.FILES.get('resume')
    newapply=Applylist.objects.create(cand=user,job=job,education=education,minsalary=minsalary,maxsalary=maxsalary,resume=resume)
    newapply.save()
   
    messages.success(request,'Applied Successfully ')
    return render(request,"Employee/Applyjob.html",{'user':user,'job':job})

