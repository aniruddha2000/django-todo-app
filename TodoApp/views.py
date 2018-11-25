from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import *
from .forms import *


@login_required(login_url='accounts:login')
def todo_view(request):
    context = {
        'todo_list': TodoList.objects.filter(user=request.user),
    }

    return render(request, "TodoApp/todo.html", context)

@login_required(login_url='accounts:login')
def add_todo(request):
    new_item = TodoList(content=request.POST.get('content'), user=request.user)
    new_item.save()
    return HttpResponseRedirect(reverse("TodoApp:todo"))

@login_required(login_url='accounts:login')
def logout_view(request):
    logout(request)
    return render(request, "TodoApp/todo.html", {"message": "Logged out."})

@login_required(login_url='accounts:login')
def delete_todo(request, todo_id):
    todo_delete = TodoList.objects.get(id=todo_id)
    todo_delete.delete()
    return HttpResponseRedirect(reverse("TodoApp:todo"))