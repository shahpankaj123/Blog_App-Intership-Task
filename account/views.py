from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import UserSignupForm,UserLoginForm


def Signup(request):
        if request.method == 'POST':
           form = UserSignupForm(request.POST)
           if form.is_valid():
             username = form.cleaned_data['username']
             password= form.cleaned_data['password']
             if User.objects.filter(username=username):
               messages.warning(request,"Username Already Taken")
               return redirect('/')
             else:
                my_user=User.objects.create_user(username,"",password)
                my_user.save()
                messages.success(request,"Account created successfully")
                return redirect('Login')
        else:
            form=UserSignupForm()    
        return render(request,'signup.html',{'form':form})  

def Login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
             username = form.cleaned_data['username']
             password= form.cleaned_data['password']
             myuser = authenticate(username=username,password=password)
             if myuser is not None:
                login(request,myuser)
                messages.success(request,"Login successfully")
                return redirect('/blog/')
             else:
               messages.warning(request,"Password or Username donot match") 
    else:
        form=UserLoginForm()              
    return render(request,'login.html',{'form':form})

def Logout(request):
   logout(request)
   return redirect('Login')

           
