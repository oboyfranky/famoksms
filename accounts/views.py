
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                if user.username.startswith('stu'):
                    return redirect("../student/dashboard")

                if user.username.startswith('tea'):
                    return redirect("../teacher/dashboard")

                if user.username.startswith('par'):
                    return redirect("../parent/dashboard")

                if user.username.startswith('sec'):
                    return redirect("../secretary/dashboard")

                if user.username.startswith('act'):
                    return redirect("../accountant/dashboard")

                if user.username.startswith('adm'):
                    return redirect("../administration/dashboard")

            
            else:
                return render(request, 'accounts/login.html', {'warning' : 'Your account is been disabled, see the administrator for futher info'})
        
        else:
            return render(request, 'accounts/login.html', {'warning' : 'Invalid Credentials, Try logging in again or see the administrator for futher info'})

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')