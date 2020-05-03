from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def home(request):
    if request.user:
        auth.logout(request)
    if request.method=='POST':
        username = request.POST['USERNAME']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            if request.user.is_superuser:

                return redirect('Manager/home')
            else:
                return redirect('Customer/home')
        else:
            messages.info(request,'invalid credentiall')
            return redirect('home')

    else:
        return render(request,'login.html')

