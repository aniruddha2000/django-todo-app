from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import *
from .forms import *


def index_view(request):
    return render(request, "TodoApp/index.html")

@login_required(login_url='TodoApp:login')
def todo_view(request):
    context = {
        'todo_list': TodoList.objects.filter(user=request.user),
    }

    return render(request, "TodoApp/todo.html", context)

@login_required(login_url='TodoApp:login')
def add_todo(request):
    new_item = TodoList(content=request.POST.get('content'), user=request.user)
    new_item.save()
    return HttpResponseRedirect(reverse("TodoApp:todo"))
        

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
    return render(request, 'TodoApp/login.html', {'form': form})

def signup_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
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
    return render(request, "TodoApp/signup.html", context)
