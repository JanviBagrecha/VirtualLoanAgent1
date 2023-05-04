from django.shortcuts import render
from adminpanel.models import Loanagent
#import mysql.connector as sql
# Create your views here.

def homepage(request):
    return render(request, 'home_page.html')

def emi(request):
    return render(request,'emi.html')

def personal_loan(request):   
    loanDetails = Loanagent.objects.all() 
    ln='pl' 
    return render(request,'loan.html',{'loanDetails':loanDetails,'ln':ln}) 

def business_loan(request):   
    loanDetails = Loanagent.objects.all() 
    ln='bl' 
    return render(request,'loan.html',{'loanDetails':loanDetails,'ln':ln}) 

def home_loan(request):   
    loanDetails = Loanagent.objects.all() 
    ln='hl' 
    return render(request,'loan.html',{'loanDetails':loanDetails,'ln':ln}) 

def education_loan(request):   
    loanDetails = Loanagent.objects.all() 
    ln='el' 
    return render(request,'loan.html',{'loanDetails':loanDetails,'ln':ln}) 

def vehicle_loan(request):   
    loanDetails = Loanagent.objects.all() 
    ln='vl' 
    return render(request,'loan.html',{'loanDetails':loanDetails,'ln':ln}) 