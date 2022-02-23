from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signup(request):
    
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        passwordC = request.POST['passwordC']
        if password == passwordC:
            User.objects.create_user(
                first_name=first_name, last_name=last_name, username=username,
                email=email, password=password
            )
            #return render(request,'home/home.html') 
            return redirect('home')  
        return render(request, 'author/signup.html', context={'invalid': True})              
    return render(request,'author/signup.html',context={'page_name':'Signup'})


def signin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            username = username,
            password = password,
        )
        if user:
            login(request,user)
            return redirect ('home')
        return render(request,'author/signin.html', context={'invalid':True,})        
    return render(request,'author/signin.html', context={'page_name':'Signin'})


def signout(request):
    logout(request)
    return redirect('home')