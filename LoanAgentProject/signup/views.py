from django.shortcuts import render,redirect
import mysql.connector as sql
fn=''
ln=''
em=''
pwd=''

# Create your views here.
def newsignup (request):
    global fn,ln,em,pwd
    if request.method=="POST":
        if request.method=="POST":
            m=sql.connect(host="localhost",user="root",password="saikamal",database='loanagent')
            cursor=m.cursor()
            d=request.POST
            for key,value in d.items():
                if key=="first_name":
                    fn=value
                if key=="last_name":
                    ln=value
                if key=="email":
                    em=value
                if key=="password":
                    pwd=value
            
            c="insert into admin Values('{}','{}','{}','{}')".format(fn,ln,em,pwd)
            cursor.execute(c)
            m.commit()
        return redirect ('http://127.0.0.1:8000/login/')
    return render(request,'signup_page.html',{})