from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.http import HttpResponse 
from .models import Account
from .forms import FormWithCaptcha
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from .forms import *


def register (request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        cpassword = request.POST.get('cpassword')
        email=request.POST.get('email')
        # dob=request.POST.get('dob')
        username = email.split('@')[0]
        # country = request.POST.get('country')
        role=request.POST.get('role')
        contact = request.POST.get('mobile')
        password = request.POST.get('password')
        # gender = request.POST.get('gender')
        is_employee=is_company=False
        print(role)
        if role=='is_employee':
            is_employee=True
        else:
            is_company=True
            print('2')
        if Account.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return render(request,'Account/register.html')
        else:
                user=Account.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password,email=email,contact=contact, is_company=is_company, is_employee=is_employee)
                user.save()
                messages.success(request, 'Thank you for registering with us. Please Activate your Email id')
                current_site = get_current_site(request)
                message = render_to_string('Account/Account_verification.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })

        send_mail(
                'Please activate your account',
                message,
                'jobportalajce@gmail.com',
                [email],
                fail_silently=False,
            )
        return redirect('/Account/login/?command=verification&email='+email)
        
    return render(request, 'Account/register.html')        
       


    
def login(request):
    print('ousside')
    if request.method=='POST':
    
        print('post')
        # username = request.POST['username']
        email = request.POST.get('email')
        password = request.POST['password']
        print(email,password)
        user=auth.authenticate(email=email,password=password)
        print(user)
        if user and user.is_active:
            auth.login(request,user)
            
            
            request.session['email'] = email
         
            if user.is_employee:
                request.session['email'] = email
                return redirect('userhome')
            if user.is_company:
                request.session['email'] = email
                return redirect('Companyhome')
            else:
                return redirect('admin/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    recaptcha = FormWithCaptcha()
    request.session.set_test_cookie()
    return render(request,'Account/login.html',{"recaptcha":recaptcha})

    
def logout(request):
    auth.logout(request)
    try:
        del request.session['email']
    except KeyError:
        pass

    return redirect('login')



def change_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = Account.objects.get(email__exact=request.user.email)
        success = user.check_password(current_password)
        if success:
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Password updated successfully.')
            return redirect('login')
        else:
            messages.error(request, 'Password does not match!')
            return redirect('change_password')
    return render(request, 'Account/Change_Password.html')


def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)

            # Reset password email


            current_site = get_current_site(request)
            message = render_to_string('Account/ResetPassword_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })

            send_mail(
                'Please activate your account',
                message,
                'jobportalajce@gmail.com',
                [email],
                fail_silently=False,
            )
            
            messages.success(request, 'Password reset email has been sent to your email address.')
            return redirect('login')
        else:
            messages.error(request, 'Account does not exist!')
            return redirect('forgotPassword')
    return render(request, 'Account/Forgot_Password.html')

def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password')
        return redirect('resetPassword')
    else:
        messages.error(request, 'This link has been expired!')
        return redirect('login')

def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successful')
            return redirect('login')
        else:
            messages.error(request, 'Password do not match!')
            return redirect('resetPassword')
    else:
        return render(request, 'Account/ResetPassword.html')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated.')
        return redirect('login')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('register')


def comp_change_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = Account.objects.get(email__exact=request.user.email)
        success = user.check_password(current_password)
        if success:
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Password updated successfully.')
            return redirect('login')
        else:
            messages.error(request, 'Password does not match!')
            return redirect('change_password')
    return render(request, 'Account/Company_changepass.html')
