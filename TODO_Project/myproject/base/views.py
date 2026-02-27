from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login_')
def home(request):
    data=TaskModel.objects.all()
    return render(request,'home.html',{'data':data})

@login_required(login_url='login_')
def add(request):
    print(request.method)
    print(request.POST)
    if request.method=='POST':
        a=request.POST['title']
        b=request.POST['desc']
        TaskModel.objects.create(
            title=a,
            desc=b
        )
        return redirect('home')
    return render(request,'add.html')

@login_required(login_url='login_')
def complete(request):
    data=completeModel.objects.all()
    
    return render(request,'complete.html',{'data':data})

@login_required(login_url='login_')
def trash(request):
    data=trashModel.objects.all()
    return render(request,'trash.html',{'data':data})

@login_required(login_url='login_')
def about(request):
    return render(request,'about.html')

@login_required(login_url='login_')
def complete_task(request,id):
    a=TaskModel.objects.get(id=id)
    completeModel.objects.create(
        title=a.title,
        desc=a.desc
    )
    a.delete()
    
    return redirect('complete')

@login_required(login_url='login_')
def trash_task(request,id):
    a=TaskModel.objects.get(id=id)
    trashModel.objects.create(
        title=a.title,
        desc=a.desc
    )
    a.delete()
    return redirect('trash')

@login_required(login_url='login_')
def delete_task(request,id):
    b=completeModel.objects.get(id=id)
    trashModel.objects.create(
        title=b.title,
        desc=b.desc
    )
    b.delete()
    return redirect('trash')

@login_required(login_url='login_')
def delete(request,id):
    a=trashModel.objects.get(id=id)
    print(a)
    a.delete()
    return redirect('trash')

@login_required(login_url='login_')
def update(request,id):
    a=TaskModel.objects.get(id=id)
    if request.method=='POST':
        a.title=request.POST['title']
        a.desc=request.POST['desc']
        a.save()
        return redirect('home')
    return render(request,'update.html',{'data':a})

@login_required(login_url='login_')
def complete_all(reqest):
    a=TaskModel.objects.all()
    for i in a:
        completeModel.objects.create(
            title=i.title,
            desc=i.desc
        )
        i.delete()
    return redirect('complete')

@login_required(login_url='login_')
def delete_all(request):
    a=TaskModel.objects.all()
    for i in a:
        trashModel.objects.create(
            title=i.title,
            desc=i.desc
        )
        i.delete()
    return redirect('trash')

@login_required(login_url='login_')
def complete_del(request):
    a=completeModel.objects.all()
    for i in a:
        trashModel.objects.create(
            title=i.title,
            desc=i.desc
        )
        i.delete()
    return redirect('trash')

@login_required(login_url='login_')
def trash_del(request):
    a=trashModel.objects.all()
    a.delete()
    return redirect('add')

@login_required(login_url='login_')
def restore(request,id):
    a=completeModel.objects.get(id=id)
    TaskModel.objects.create(
        title=a.title,
        desc=a.desc
    )
    a.delete()
    return redirect('home')

@login_required(login_url='login_')
def restore_all(request):
    a=completeModel.objects.all()
    for i in a:
        TaskModel.objects.create(
            title=i.title,
            desc=i.desc
        )
    a.delete()
    return redirect('home')

