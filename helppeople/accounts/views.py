from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth

# Create your views here.
from django.shortcuts import render
from django.contrib import messages,

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        user = User.objects.create_user(username=username, email=email, password=confirm_password)
        user.save()
        print('user created')
        return redirect('/')

    else:        
        return render(request, 'signup.html')





def signin(request):
    return render(request, 'signin.html')