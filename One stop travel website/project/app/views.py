import sys

from app.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser, User
from django.shortcuts import redirect, render


def index(request):
     return render(request,'index.html')

def about(request):
     return render(request,'about.html')

def chardham(request):
     return render(request,'chardham.html')

def ad(request):
     return render(request,'ad.html')

def amritsar(request):
     return render(request,'amritsar.html')

def kerala(request):
     return render(request,'kerala.html')

def ladakh(request):
     return render(request,'ladakh.html')

def lakshdweep(request):
     return render(request,'lakshdweep.html')

def manali(request):
     return render(request,'manali.html')

def hp(request):
     return render(request,'hp.html')

def goa(request):
     return render(request,'goa.html')

def uttarakhand(request):
     return render(request,'uttarakhand.html')

def udaipur(request):
     return render(request,'udaipur.html')



def loginUser(request):
    
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)
        if user is not None:
           
            login(request, user)
            return redirect('index')
        else:
           
            return render( request,'login.html')
        
    return render(request,'login.html')

def signupUser(request):
    
    if request.method == 'POST':

        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')   
        username=fname
        if(pass1 != pass2):
           
            return redirect('signup')
        
        # Code for password check

        Myuser = User.objects.create_user(username, email, pass1)
        Myuser.save()
        # update = User.objects.all().filter(username = username)
        # update.firstname = fname
        # update.lastname = lname
        return redirect('login')

    return render(request,'signup.html')

def logoutUser(request):
     logout(request)

     return redirect('login')