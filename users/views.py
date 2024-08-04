from django.shortcuts import render, redirect
from . forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request,user)
            return redirect('cinema_app:movie')
    else:
        form = SignUpForm()
    return render(request, 'users/register.html',{'form':form})


def signin(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('cinema_app:movie')
            else:
                messages.error(request, 'Invalid Username or Password. ')
                
        else:
            messages.error(request, 'Invalid Username or Password. ')
    else:
        form = LoginForm()
    return render(request, 'users/login.html',{'form':form})


def signout(request):
    logout(request)
    return redirect('user:signup')