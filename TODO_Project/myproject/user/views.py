from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def register_(request):
    if request.method=="POST":
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        print(fname,lname,email,username,password)
        try:
            a=User.objects.get(username=username)
            return render(request,'register_.html',{'status':True})
        except:
            v=User.objects.create_user(
                first_name=fname,
                last_name=lname,
                email=email,
                username=username,
                
            )
            v.set_password(password)
            v.save()        
            
    return render(request,'register_.html')

def login_(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        u=authenticate(username=username,password=password)
        if u:
            login(request,u)
            return redirect('add')
        else:
            return render(request,'login_.html',{'status':True})
    return render(request,'login_.html')

@login_required(login_url='login_')
def logout_(request):
    logout(request)
    return redirect('login_')

@login_required(login_url='login_')
def profile(request):
    return render(request,'profile.html')

@login_required(login_url='login_')
def reset_pass(request):
    if request.method=='POST':
        if 'oldpass' in request.POST:
            a=request.POST['oldpass']
            auth=authenticate(username=request.user.username,password=a)
            if auth:
                return render(request,'reset_pass.html',{'new_pass':True})
            else:
                return render(request,'reset_pass.html',{'wrong':True})
        if 'newpass' in request.POST:
            b=request.POST['newpass']
            if request.user.check_password(b):
                return render(request,'reset_pass.html',{'same':True})
            request.user.set_password(b)
            request.user.save()
            return redirect('login_')
    return render(request,'reset_pass.html')


def forget_pass(request):
    if request.method=="POST":
        a=request.POST['username']
        try:
            a=User.objects.get(username=a)
            request.session['fp_user']=a.username
            return redirect('new_password')
        except:
            return render(request,'forget_pass.html',{'error':True})
    return render(request,'forget_pass.html')

def new_password(request):
    if request.method=="POST":
        username=request.session.get('fp_user')
        if username is None:
            return redirect('forget_pass')
        user=User.objects.get(username=username)
        if request.method=='POST':
            new=request.POST['newpass']
            if user.check_password(new):
                return render(request,'new_password.html',{'error':True})
            user.set_password(new)
            user.save()
            del request.session['fp_user']
            return redirect('login_')
    return render(request,'new_password.html')