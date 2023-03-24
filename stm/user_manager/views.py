from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from django.http.response import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')


def login(request):
    
    if request.method == 'POST':

        username = request.POST.get('username', False)
        password = request.POST.get('password', False)

        user = auth.authenticate(username=username, password=password)
         
        if user is not None:
            auth.login(request, user)
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            request.session['first_name'] = user.first_name
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'login_register.html')
     

def register(request):
    
    if request.method == 'POST':

        first_name = request.POST.get('first_name', False)
        last_name = request.POST.get('last_name', False)
        username = request.POST.get('username', False)
        email = request.POST.get('email', False)
        password = request.POST.get('password', False)
        re_password = request.POST.get('repeat_password', False)



        if password != re_password:
            messages.info(request, "Password not matching")
            messages.info(request, "Please Try Again")

        elif User.objects.filter(username=username).exists():
            messages.info(request, "Username Already Taken")
            messages.info(request, "Please Try Again")

        elif User.objects.filter(email=email).exists():
            messages.info(request, "Email ID Already Taken")
            messages.info(request, "Please Try Again")

        else:
            user = User.objects.create_user(first_name=first_name,
                                        last_name=last_name,
                                        username=username,
                                        email = email,
                                        password=password)
            user.save()
            messages.info(request, "User Created!")

    return redirect('login')

def logout(request):
    auth.logout(request)
    return redirect('/')