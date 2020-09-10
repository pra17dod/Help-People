from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.info(request,'Welcome!')
                return redirect('/')
            else:
                messages.info(request, 'Invalid username or password')
                return redirect('signin')
        else:
            messages.info(request, 'User not found, signup first!')
            return redirect('signup')

    else:
        return render (request, 'signin.html')

def signup(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password'] 

        if password1 == password2:     
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists")
                return redirect('signup')  
            elif User.objects.filter(email=email).exists():   
                messages.info(request,"Email already exists")
                return redirect('signup')  
            else:        
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)          
                user.save()
                messages.info(request,"User created")
                return redirect('signin')              
        else:
            messages.info(request, "Password not matching") 
            return redirect('signup')  
    else:    
        return render(request,'signup.html')

def signout(request):
    auth.logout(request)
    messages.info(request, "Thank you! See you soon")
    return redirect('/')