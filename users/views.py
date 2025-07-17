from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import LoginForm

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/users/')
            else:
                return HttpResponse("invalid credentials")
    else:
        form = LoginForm()
    return render(request,'users/login.html',{'form':form})

@login_required
def index(request):
    return render(request,'users/index.html')

def user_logout(request):
    logout(request)
    return render(request, 'users/logout.html')