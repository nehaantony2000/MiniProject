from django.shortcuts import render

# Create your views here.

def res(request):
    return render(request,'resume.html')