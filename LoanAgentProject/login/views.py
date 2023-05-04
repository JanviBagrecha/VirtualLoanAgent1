from django.shortcuts import render,redirect
import mysql.connector as sql
from django.contrib import messages

em=''
pwd=''
# Create your views here.
def adminlogin (request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="saikamal",database='loanagent')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="select * from admin where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            messages.warning(request, "Invalid Account!! Please make an account!!")
            #return redirect('http://localhost:8000/signup/')
        else:
            return redirect('/adminpanel')

    return render(request,'login_page.html') 