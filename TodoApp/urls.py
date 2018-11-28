from django.urls import path
from TodoApp import views


app_name = 'TodoApp'
urlpatterns = [
    path("add", views.add_todo, name="AddTodo"),
    path("todo", views.todo_view, name="todo"),
    path("delete/<int:todo_id>", views.delete_todo, name="DeleteTodo")
]
