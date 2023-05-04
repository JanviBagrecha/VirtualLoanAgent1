"""
URL configuration for LoanAgentProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from signup.views import newsignup
from login.views import adminlogin
from adminpanel.views import index,edit,update,destroy,addnew
from home.views import homepage,emi,personal_loan,business_loan,home_loan,education_loan,vehicle_loan
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    path('admin/', admin.site.urls),
    path('signup/',newsignup),
    path('login/',adminlogin),
    path('adminpanel/', index, name='index'),  
    path('adminpanel/addnew/',addnew,name = 'addnew'),  
    path('adminpanel/edit/<int:id>', edit, name='edit'),  
    path('adminpanel/update/<int:id>', update, name='update'),  
    path('adminpanel/delete/<int:id>', destroy, name='destroy'),
    path("",homepage),
    path("emi/",emi),
    path("personalloan/",personal_loan),
    path("businessloan/",business_loan),
    path("homeloan/",home_loan),
    path("educationloan/",education_loan),
    path("vehicleloan/",vehicle_loan),
]

urlpatterns += staticfiles_urlpatterns()