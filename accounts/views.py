from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import *
from .forms import *

def index_view(request):
    return render(request, "accounts/index.html")

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('TodoApp:todo')
    return render(request, 'accounts/login.html', {'form': form})

def signup_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('TodoApp:todo')

    context = {
        'form': form,
    }
    return render(request, "accounts/signup.html", context)

def update_password_view(request):
    next = request.GET.get('next')
    form = UpdatePassword(data=request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('new_password1')
        user.set_password(password)
        user.save()
        if next:
            return redirect(next)
        return redirect('TodoApp:todo')

    context = {
        'form': form,
    }
    return render(request, "accounts/update_pass.html", context)