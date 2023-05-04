# Create your views here.
from django.shortcuts import render, redirect  
from adminpanel.forms import loanForm
from adminpanel.models import Loanagent
import mysql.connector as sql
id=""
nm=""
ipl=""
ibl=""
ihl=""
iel=""
ivl=""
ppl=""
pbl=""
phl=""
pel=""
pvl=""
tpl=""
tbl=""
thl=""
tel=""
tvl=""
#Create your views here.  
def addnew(request): 
    global nm,ipl,ibl,ihl,iel,ivl,ppl,pbl,phl,pel,pvl,tpl,tbl,thl,tel,tvl
    if request.method == "POST":  
        if request.method=="POST":
            m=sql.connect(host="localhost",user="root",password="saikamal",database='loanagent')
            cursor=m.cursor()
            forms = request.POST  
            for key,value in forms.items():
                    if key=="name":
                        nm=value
                    if key=="interest_pl":
                        ipl=value
                    if key=="interest_bl":
                        ibl=value
                    if key=="interest_hl":
                        ihl=value
                    if key=="interest_el":
                        iel=value
                    if key=="interest_vl":
                        ivl=value
                    if key=="principal_pl":
                        ppl=value
                    if key=="principal_bl":
                        pbl=value
                    if key=="principal_hl":
                        phl=value
                    if key=="principal_el":
                        pel=value
                    if key=="principal_vl":
                        pvl=value
                    if key=="time_pl":
                        tpl=value
                    if key=="time_bl":
                        tbl=value
                    if key=="time_hl":
                        thl=value
                    if key=="time_el":
                        tel=value
                    if key=="time_vl":
                        tvl=value
                    
            c="insert into bankdetails(name,interest_pl,interest_bl,interest_hl,interest_el,interest_vl,principal_pl,principal_bl,principal_hl,principal_el,principal_vl,time_pl,time_bl,time_hl,time_el,time_vl) Values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(nm,ipl,ibl,ihl,iel,ivl,ppl,pbl,phl,pel,pvl,tpl,tbl,thl,tel,tvl)
            cursor.execute(c)
            m.commit()
        return redirect('/adminpanel')
    else:
        form = loanForm()  
    return render(request,'index.html',{'form':form})
    #return render(request,'addnew.html',{})  
     #redirect("http://localhost:8000/adminpanel") 
 
def index(request):  
    loanDetails = Loanagent.objects.all()  
    return render(request,'show.html',{'loanDetails':loanDetails})  
 
def edit(request,id):  
    loanDetails = Loanagent.objects.get(id=id)  
    return render(request,'edit.html', {'loanDetails':loanDetails})  
 
def update(request,id):  
    loanDetails = Loanagent.objects.get(id=id)
    global nm,ipl,ibl,ihl,iel,ivl,ppl,pbl,phl,pel,pvl,tpl,tbl,thl,tel,tvl
    if request.method == "POST":  
        if request.method=="POST":
            m=sql.connect(host="localhost",user="root",password="saikamal",database='loanagent')
            cursor=m.cursor()
            forms = request.POST  
            for key,value in forms.items():
                    if key=="name":
                        nm=value
                    if key=="interest_pl":
                        ipl=value
                    if key=="interest_bl":
                        ibl=value
                    if key=="interest_hl":
                        ihl=value
                    if key=="interest_el":
                        iel=value
                    if key=="interest_vl":
                        ivl=value
                    if key=="principal_pl":
                        ppl=value
                    if key=="principal_bl":
                        pbl=value
                    if key=="principal_hl":
                        phl=value
                    if key=="principal_el":
                        pel=value
                    if key=="principal_vl":
                        pvl=value
                    if key=="time_pl":
                        tpl=value
                    if key=="time_bl":
                        tbl=value
                    if key=="time_hl":
                        thl=value
                    if key=="time_el":
                        tel=value
                    if key=="time_vl":
                        tvl=value
                
            c="update bankdetails set name='{}',interest_pl='{}',interest_bl='{}',interest_hl='{}',interest_el='{}',interest_vl='{}',principal_pl='{}',principal_bl='{}',principal_hl='{}',principal_el='{}',principal_vl='{}',time_pl='{}',time_bl='{}',time_hl='{}',time_el='{}',time_vl ='{}' where id='{}'".format(nm,ipl,ibl,ihl,iel,ivl,ppl,pbl,phl,pel,pvl,tpl,tbl,thl,tel,tvl,id)  
            cursor.execute(c)
            m.commit() 
    return redirect("http://localhost:8000/adminpanel/")
     
def destroy(request, id):  
    loanDetails = Loanagent.objects.get(id=id)  
    loanDetails.delete()  
    return redirect("http://localhost:8000/adminpanel/") 
