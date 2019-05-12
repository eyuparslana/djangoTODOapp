from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def register_view(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        confirmpass = request.POST['confirmpass']
        if not username or not password or not confirmpass:
            return render(request, 'accounts/register.html', {'error': 'Please enter username/passwords'})
        user = User.objects.filter(username=username)
        if user:
            return render(request, 'accounts/register.html', {'error': 'Username already exist!'})
        if password != confirmpass:
            return render(request, 'accounts/register.html', {'error': 'Passwords are must match!'})
        User.objects.create(username=username, password=password)
        return redirect('/accounts/login')
    return render(request, 'accounts/register.html')


def login_view(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        if not username or not password:
            return render(request, 'accounts/login.html', {'error': 'Please enter username/passwords'})
        user = User.objects.get(username=username, password=password)
        if not user:
            return render(request, 'accounts/login.html', {'error': 'Wrong username/passwords!'})
        else:
            login(request, user)
            return redirect('/todo/')
    return render(request, 'accounts/login.html')


def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    logout(request)
    return redirect('/accounts/login')
