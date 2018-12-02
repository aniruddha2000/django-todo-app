from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import *
from .forms import *


# @login_required(login_url='accounts:login')
# def todo_view(request):
#     """
#         This function for showing all todos
#     """
#     context = {
#         'todo_list': TodoList.objects.filter(user=request.user),
#     }

#     return render(request, "TodoApp/todo.html", context)

@login_required(login_url='accounts:login')
def todo_view(request):
    """
        This function for adding todo 
    """
    # new_item = TodoList(content=request.POST.get('content'), user=request.user)
    # new_item.save()
    # return HttpResponseRedirect(reverse("TodoApp:todo"))
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
    context = {
        'todo': todo_edit,
    }
    if request.method == 'POST':
        content = request.POST.get('content')
        todo_edit.content = content
        todo_edit.save()
    else:
        return render(request, 'TodoApp/edit_todo.html', context)