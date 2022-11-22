from django.shortcuts import render,redirect
import sweetify
from Account.models import Account,JobDetails,Applylist
from django.contrib import messages, auth

def Companyhome(request):
    p=JobDetails.objects.all()
    return render(request,'Comp/index.html',{'p':p})

def postjob(request):
    return render(request,'Comp/JobPost.html')

def postedjob(request):
     p=JobDetails.objects.all()
     return render(request, 'Comp/Postedjoblist.html',{'p':p})
def profile(request):
    return render(request, 'Comp/Company_profile.html')
 
def JobdetailSubmit(request):
    user=Account.objects.get(email=request.session.get('email'))
    if request.user.is_company:
       jobname=request.POST['jobname']
       companyname=request.POST['Cname']
       companyaddress=request.POST['add']
       jobdescription=request.POST['Description']
       qualification=request.POST['qualification']
       responsibility=request.POST['Response']
       location=request.POST['location']
       experience=request.POST['exp']
       salarypackage=request.POST['salary']
       companywebsite=request.POST['web']
       logo=request.POST['logo']
       companycontact=request.POST['mobile']
       companyemail=request.POST['email']
       newjob=JobDetails.objects.create(jobname=jobname,companyname=companyname,companyaddress=companyaddress,qualification=qualification,jobdescription=jobdescription,responsibility=responsibility,location=location,experience= experience,companyemail=companyemail,companycontact=companycontact,companywebsite=companywebsite,salarypackage=salarypackage,logo=logo )
       messages.success(request,'Job Posted ')
       return render(request,"Comp/jobPost.html")
        

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
        profilepic =request.POST.get('pic')
        jobtype=request.POST.get('jobtype')
        # skills=request.POST.get('skills')
        # languages=request.POST.get('languages')
        # education = request.POST.get('education')
        user_id = request.user.id
        
        user = Account.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.contact = contact
        user.address = address
        user.district=district
        user.country=country
        user.state=state
        user.jobtype=jobtype
        user.profilepic =profilepic 
        user.save()
        sweetify.success(request,'Profile Are Successfully Updated. ')
        return redirect('profile')

def JobApplylist(request):
    Apply=Applylist.objects.all()
    return render(request,"Comp/Applylist.html",{'Apply':Apply})      