from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
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
    form = ChangePasswordForm(data=request.POST, user=request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('TodoApp:todo')

    context = {
        'form': form,
    }
    return render(request, "accounts/update_pass.html", context)

@login_required(login_url='accounts:login')
def logout_view(request):
    logout(request)
    return redirect('accounts:login')