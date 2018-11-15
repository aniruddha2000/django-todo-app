from django.urls import path
from TodoApp import views


app_name = 'TodoApp'
urlpatterns = [
    path("", views.index_view, name="index"),
    path("login", views.login_view, name="login"),
    path("signup", views.signup_view, name="signup"),
    path("add", views.add_todo, name="AddTodo"),
    path("todo", views.todo_view, name="todo"),
]
