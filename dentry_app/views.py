from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from dentry_app.models import Product,Image
from django.db.models import Q


# Create your views here.
def home(request):
    print(request.user.is_authenticated)
    user=request.user.username
    context={}
    context['products']=Product.objects.filter(is_active=True)  
    return render(request,'index.html',context)



def user_login(request):
    if request.method=="POST":
        uemail=request.POST['uemail']
        upass=request.POST['upass']
        if uemail=='' or upass=='':
            context={}
            context['errmsg']="Feild should not be empty"
            return render(request,'login.html,context')
        else:
            u=authenticate(username=uemail,password=upass)
            print(u)
            if u is not None:
                login(request,u)
                return redirect('/home')
            else:
                context={}
                context['errmsg']="Invalid entry"
                return render(request,'login.html',context)
    else:
        return render(request,'login.html') 
        
        
def user_register(request):
    if request.method=='POST':
        uemail=request.POST['uemail']
        upass=request.POST['upass']
        ucpass=request.POST['ucpass']
        if uemail=="" or upass=="" or ucpass=="":
            context={}
            context['errmsg']="Feild cannot be empty"
            return render(request,'register.html',context)
        elif upass!=ucpass:
            context={}
            context['errmsg']="Password didnt match"
            return render(request,'register.html',context)
        else:
            try:
                u=User.objects.create(username=uemail,password=upass,email=uemail)
                u.set_password(upass)
                u.save()
                context={}
                context['success']="user created successfully, please Login"
                return render(request,'register.html',context)
            except Exception:
                context={}
                context['errmsg']="user with same username already Exits!!"
                return render(request,'register.html', context)         
    else:
        return render(request,'register.html')
    
    
    
def user_logout(request):
    logout(request)
    return redirect('/home')

def product(request,pid):
    p=Product.objects.filter(id=pid)
 #  print(p)
    #return HttpResponse(pid)
    context={}
    context['products']=p
    return render(request,'product_details.html',context)

def imgdisplay(request):
    
    return HttpResponse("image 1 ")
