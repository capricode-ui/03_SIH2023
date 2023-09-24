from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth


def index(request):
    return render(request,'index.html')

# def login(request):
#     return render(request,'login.html')

# def signup(request):
#     return render(request,'Sign_up.html')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email =request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Email is exist ')
                return redirect(signup)
            else:
                user = User.objects.create_user(username=username,
                password=password, email=email, first_name=first_name, last_name=last_name)
                user.set_password(password)
                user.save()
                print("success")
                return redirect('login')
        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(signup)
    else:
        print("no post method")
        return render(request, 'Sign_up.html') 

def login(request):
    if request.method == 'POST':
        username =request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login')
    else:
        return render(request, 'login.html') 

def logout_user(request):
    auth.logout(request)
    return redirect('index') 


    

# Create your views here.
