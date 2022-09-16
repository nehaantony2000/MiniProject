
from django.shortcuts import render




def index(request):
    return render(request,'index.html')
def userhome(request):
    return render(request,'userhome.html')
def adminhome (request):
        return render(request,'Adminhome.html')
def companyhome (request):
        return render(request,'CompanyHome.html')
