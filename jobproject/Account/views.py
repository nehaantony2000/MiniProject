from django.shortcuts import render

# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('http://127.0.0.1:8000/Main/')
        else:
            messages.info(request,"please register")
            return render(request,'register.html')
    else:
        return render(request,'login.html')
def register (request):
    if request.method=='POST':
        username = request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        email=request.POST['email']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('/Account/register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return render('/Account/register/')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password,email=email)
                user.save()
                return redirect('/Account/login/')
        else:
            print('pass not matching')
            return redirect('register.html')
    else:
        return render(request,'register.html')