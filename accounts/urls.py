from django.urls import path
from accounts import views
from django.conf import settings


app_name = 'accounts'
urlpatterns = [
    path("", views.index_view, name="index"),
    path("login", views.login_view, name="login"),
    path("signup", views.signup_view, name="signup"),
    path("password&update", views.update_password_view, name="pass_update"),
    path("logout", views.logout_view, name="logout"),
]
