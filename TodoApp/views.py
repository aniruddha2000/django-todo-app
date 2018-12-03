from django.shortcuts import (
    render, 
    redirect, 
    get_object_or_404,
)
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


@login_required(login_url='accounts:login')
def todo_view(request):
    """
        This function for adding todo 
    """
    form = TodoForm(request.POST or None)
    if form.is_valid():
        new_todo = TodoList(content=form.cleaned_data.get('todo'), user=request.user)
        new_todo.save()
        return redirect('TodoApp:todo')

    context = {
        'form': form,
        'todo_list': TodoList.objects.filter(user=request.user),
    }
    return render(request, "TodoApp/todo.html", context)

@login_required(login_url='accounts:login')
def delete_todo(request, todo_id):
    """
        This function for deleting todo
    """
    todo_delete = TodoList.objects.get(id=todo_id)
    todo_delete.delete()
    return redirect("TodoApp:todo")

@login_required(login_url='accounts:login')
def edit_todo(request, todo_id):
    """
        This function for edditing todo
    """
    todo_edit = TodoList.objects.get(id=todo_id)
    form = TodoForm(request.POST or None, instance=todo_edit)
    if form.is_valid():
        item = form.save(commit=False)
        content = form.cleaned_data.get('todo')
        item.content = content
        item.save()
        return redirect('TodoApp:todo')

    context = {
        'form': form,
        'item': todo_edit,
    }
    return render(request, "TodoApp/edit_todo.html", context)
