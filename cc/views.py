from django.shortcuts import render
import faker


#generator function
def cc(g):
    k=[]
    f = faker.Faker()
    for i in range(0,g):
        m=f.credit_card_full()
        k.append(m)
    return k

def fakeprofile(s,n):
    k=[]
    f = faker.Faker()
    for i in range(0,n):
        m=f.simple_profile(sex=s)
        k.append(m)
    return k


def email(n):
    k=[]
    f = faker.Faker()
    for i in range(0,n):
        m=f.ascii_free_email()
        k.append(m)
    return k
    
    
    
    
    
    
    
    
    
    
#django function 
def index(request):
    
    return render(request,'index.html')

def ccsearch(request):
    g=request.POST['value']
    g=int(g)
    k=cc(g)
    return render(request,"index.html",{'k':k})

def profile(request):
    return render(request,'AboutME.html')


def fprofile(request):
    g=request.POST['value']
    g=int(g)
    s='M'
    k=fakeprofile(s,g) 
    return render(request,'AboutME.html',{"D":k})



def mail(request):
    return render(request,'mail.html')


def fmail(request):
    g=request.POST['value']
    n=int(g)
    k=email(n)
    return render(request,'mail.html',{"D":k})
