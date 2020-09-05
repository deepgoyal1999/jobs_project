from django.shortcuts import render
from recruiter.models import hydjobinfo,mumbaijobinfo,delhijobinfo
# Create your views here.
def delhijobdata(request):
    jobs_list=delhijobinfo.objects.all()
    return render(request,"recruiter/delhi.html",{'jobs_list':jobs_list})

def hydjobdata(request):
    jobs_list=hydjobinfo.objects.all()
    return render(request,"recruiter/hyd.html",{'jobs_list':jobs_list})

def mumbaijobdata(request):
    jobs_list=mumbaijobinfo.objects.all()
    return render(request,"recruiter/mumbai.html",{'jobs_list':jobs_list})

def home(request):
    return render(request,"recruiter/home.html")
