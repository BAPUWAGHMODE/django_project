from django.shortcuts import render,HttpResponseRedirect
from .models import employee
from .forms import employeeregistarion,employeeregistrationForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def added(request):
    if request.method=='POST':
        fm=employeeregistarion(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
    else:
        fm=employeeregistarion()
    pi=employee.objects.all()
    return render(request,'enroll/add.html',{'form':fm,'pi':pi})

def delete(request,id):
    if request.method=='POST':
        pi=employee.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/add')

def update(request,id):
    if request.method=='POST':
        pi=employee.objects.get (pk=id)
        fm=employeeregistarion(request.POST,request.FILES,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=employee.objects.get(pk=id)
        fm=employeeregistarion(instance=pi)
    return render(request,'enroll/update.html',{'form':fm,'pi':pi})

def signin(request):
    if request.method=='POST' :
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=UserCreationForm()
    return render(request,'enroll/signin.html',{'form':fm})

def sign_up(request):
    if request.method=='POST':
        fm=employeeregistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=employeeregistrationForm()
    return render(request,'enroll/sign _up.html',{'form':fm})

def login1(request):
        if request.user.is_authenticated:
            if request.method=='POST':
                fm=AuthenticationForm(request=request,data=request.POST)
                if fm.is_valid():
                    uname=fm.cleaned_data['username']
                   upass=fm.cleaned_data['password']
                    user=authenticate(username=uname,password=upass)
                if user is not None:
                        login(request,user)
                        return HttpResponseRedirect('/add/')
            else:
                fm=AuthenticationForm()
            return render(request,'enroll/login.html',{'form':fm})

        else:
            return HttpResponseRedirect('/login/')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/sign_up/')
