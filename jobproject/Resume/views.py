
from fileinput import filename
from django.http import HttpResponse, JsonResponse, response
from django.shortcuts import render, redirect,reverse
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout
from django.template import context
from Account.models import Skill,Academic,Referee,Profile,Skill,Account
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password
import pdfkit







@login_required
def dashboard(request):
    user_id = request.user.id

    try:
        cv_id = Account.objects.filter(user_id=user_id).values_list('id', flat=True)
        cv_id = list(cv_id)
        cv_id = cv_id[0]
        print('Cv ID is',cv_id)
        print('Data type',type(cv_id))
        if isinstance(cv_id, int):
            context = {'status':'there_is_cv'}
            return render(request, 'Resume/resume.html', context)
    except Exception as e:
        context = {'status':'no_cv'}
        return render(request, 'Resume/resume.html', context)    



def createCv(request):
    user_id = request.user.id

    try:
        cv_id = Account.objects.filter(user_id=user_id).values_list('id', flat=True)
        cv_id = list(cv_id)
        cv_id = cv_id[0]

        profile_id = Profile.objects.filter(cv_id=cv_id).values_list('id', flat=True)
        profile_id = list(profile_id)
        profile_id = profile_id[0]

        if isinstance(profile_id, int):
            context = {'status':'there_is_profile'}
            return render(request, 'Resume/create_cv.html', context)
    except Exception as e:
        context = {'status':'no_profile'}
        return render(request, 'Resume/create_cv.html', context)




def saveSkill(request):
    if request.method == 'POST':
        user_id = request.user.id
        
        cv_id = Account.objects.filter(user_id=user_id).values_list('id', flat=True)
        cv_id = list(cv_id)
        cv_id = cv_id[0]


        s_name = request.POST.getlist('s_name[]')
        s_level = request.POST.getlist('s_level[]')
        
        if(len(s_name) == 1):
            a = Skill(s_name = s_name[0], s_level=s_level[0], cv_id=cv_id)
            a.save()
            return JsonResponse({'status':1})
        else:
            for x,y in zip(s_level,s_name):
                a = Skill(s_level=x, s_name=y, cv_id=cv_id)
                a.save()
            return JsonResponse({'status':1})
    return JsonResponse({'status':0})
                



def saveEducation(request):
    if request.method == 'POST':
        name = request.POST.getlist('name[]')
        year = request.POST.getlist('year[]')
        award = request.POST.getlist('award[]')


        user_id = request.user.id
        cv_id = Account.objects.filter(user_id=user_id).values_list('id', flat=True)
        cv_id = list(cv_id)
        cv_id = cv_id[0]



        if(len(name) == 1):
            a = Academic(a_institution = name[0], a_year=year[0], a_award=award[0], cv_id=cv_id)
            a.save()
            return JsonResponse({'status':1})
        else:
            for x,y,z in zip(name,year,award):
                a = Academic(a_institution=x, a_year=y, a_award=z, cv_id=cv_id)
                a.save()
            return JsonResponse({'status':1})
    return JsonResponse({'status':0})




def saveReferee(request):
    if request.method == 'POST':
        name = request.POST.getlist('name[]')
        phone = request.POST.getlist('phone[]')
        email = request.POST.getlist('email[]')

        user_id = request.user.id
        cv_id = Account.objects.filter(user_id=user_id).values_list('id', flat=True)
        cv_id = list(cv_id)
        cv_id = cv_id[0]

        if(len(name) == 1):
            a = Referee(r_name = name[0], r_email=email[0], r_phone=phone[0], cv_id=cv_id)
            a.save()
            return JsonResponse({'status':1})
        else:
            for x,y,z in zip(name,phone,email):
                a = Referee(r_name=x, r_phone=y, r_email=z, cv_id=cv_id)
                a.save()
            return JsonResponse({'status':1})
    return JsonResponse({'status':0})





def uploadProfile(request):
    fname = request.POST.get('fname')
    mname = request.POST.get('mname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    gender = request.POST.get('gender')
    bio = request.POST.get('bio')
    dob = request.POST.get('dob')
    occupation = request.POST.get('occupation')
    country = request.POST.get('country')
    region = request.POST.get('region')
    file = request.FILES.get('file')
    user_id = request.user.id

    Account.objects.create(user_id=user_id)

    cv_id = Account.objects.filter(user_id=user_id).values_list('id', flat=True)
    cv_id = list(cv_id)
    cv_id = cv_id[0]
    print('Cv ID is',cv_id)



    p = Profile(fname=fname, mname=mname, lname=lname, email=email, bio=bio, dob=dob, gender=gender, occupation=occupation, country=country, region=region, avator=file,phone=phone,cv_id=cv_id)
    p.save()

    return JsonResponse({'status':1})


def updateAcademic(request):
    id = request.POST.get('id')
    institution = request.POST.get('institution')
    year = request.POST.get('year')
    award = request.POST.get('award')


    Academic.objects.filter(id=id).update(a_institution=institution, a_year=year, a_award=award)

    return JsonResponse({'status':1})



def updateProfile(request):
    id = request.POST.get('id')
    fname = request.POST.get('fname')
    mname = request.POST.get('mname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    gender = request.POST.get('gender')
    bio = request.POST.get('bio')
    dob = request.POST.get('dob')
    occupation = request.POST.get('occupation')
    country = request.POST.get('country')
    region = request.POST.get('region')
    file = request.FILES.get('file')

    user_id = request.user.id
    cv_id =Account.objects.filter(user_id=user_id).values_list('id', flat=True)
    cv_id = list(cv_id)
    cv_id = cv_id[0]

    Profile.objects.filter(cv_id=id).update(fname=fname, mname=mname, lname=lname, email=email, bio=bio, dob=dob, gender=gender, occupation=occupation, country=country, region=region, avator=file,phone=phone,cv_id=cv_id)

    return JsonResponse({'status':1})










def viewPDF(request, id=None):
    user_profile = Profile.objects.filter(cv_id=id)
    user_skill = Skill.objects.filter(cv_id=id).values()
    user_referee = Referee.objects.filter(cv_id=id).values()
    user_education = Academic.objects.filter(cv_id=id).values()


    context = {'user_profile':user_profile,'user_skill':user_skill,'user_referee':user_referee,'user_education':user_education}
    return render(request, 'Resume/pdf_template.html', context)



def editCv(request):
    return render(request, 'Resume/edit_cv.html')


def fetchProfile(request):
    id = request.POST.get('id')
    print('Cv ID is',id)
    
    user_profile = Profile.objects.get(cv_id=id)


    user_profile = {'fname':user_profile.fname, 
    'mname':user_profile.mname,
    'lname':user_profile.lname,
    'email':user_profile.email,
    'phone':user_profile.phone,
    'bio':user_profile.bio,
    'dob':user_profile.dob,
    'country':user_profile.country,
    'region':user_profile.region,
    'occupation':user_profile.occupation
    }
    return JsonResponse(user_profile)



def fetchAcademic(request):
    id = request.POST.get('id')
    print('Cv ID is',id)
    
    user_education = Academic.objects.get(id=id)

    user_education = {'institution':user_education.a_institution, 
    'year':user_education.a_year,
    'award':user_education.a_award
    }
    return JsonResponse(user_education)




def deleteProfile(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        print('Cv ID is',id)
        
        user_profile = Profile.objects.get(cv_id=id)
        user_profile.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})





def deleteAcademic(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        print('Cv ID is',id)
        
        user_education = Academic.objects.get(id=id)
        user_education.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})



def educationView(request):
    id = request.user.cv.id
    print('Cv ID is',id)
    user_education = Academic.objects.filter(cv_id=id).all()
    context = {'user_education':user_education}
    return render(request, 'core/education_view.html', context)



def generate_PDF(request, id):
    print('Download Cv Id is',id)
    pdf = pdfkit.from_url(request.build_absolute_uri(reverse('cv-detail', args=[id])), False)
    response = HttpResponse(pdf, content_type='application/pdf') 
    response['Content-Disposition'] = 'attachment; filename="cv.pdf"'
    return response


