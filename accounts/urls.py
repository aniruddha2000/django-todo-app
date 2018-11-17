from django.urls import path
from accounts import views


app_name = 'accounts'
urlpatterns = [
    path("", views.index_view, name="index"),
    path("login", views.login_view, name="login"),
    path("signup", views.signup_view, name="signup"),
]
