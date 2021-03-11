from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# from .forms import UserRegisterForm

# Create your views here.
# def signup(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('index.html')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'signup.html', {'form': form})





# def signin(request):
#     return render(request, 'signin.html')

# def signup(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         password1 = request.POST['password']
#         confirm_password = request.POST['confirm_password']
        
#         user = User.objects.create_user(username=username, email=email, password=confirm_password)
#         user.save()
#         print('user created')
#         return redirect('/')

#     else:        
#         return render(request, 'signup.html')

# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User, auth
# from django.shortcuts import render
# from django.contrib import messages

# # Create your views here.

def signup(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2'] 

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
 



def signin(request):
    return render(request, 'signin.html')