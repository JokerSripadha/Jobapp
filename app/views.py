from django.shortcuts import render,redirect
from django.http import HttpResponse
from app import *
from django.template import  loader
from django.urls import reverse
from app.models import JobPost
# Create your views here.
job_title =[
    'First job','Second job'
]
job_decription =[
    '1st job description','2nd job description'
]



def hello(request):
    
    list=['your','so','awesome']
    is_auth= False
    context={'name':'Sripadha','list':list,'is_auth':is_auth}
   
    return render(request,'hello.html',context)
def job_list(request):
   
    jobs=JobPost.objects.all()
    
    
    
    context={'job_title':jobs}
    
    return render(request,'index.html',context)
   
     

def job_detail(request,id):
    
    jobs=JobPost.objects.get(id=int(id))
    context={'job':jobs}
    return render(request,'jobs_home.html',context)
    
    