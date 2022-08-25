from django.urls import path
from . import views
from django.contrib.auth import views as av

urlpatterns = [
    path("login", views.user_login, name="login"),
    path("logout", views.UserLogoutView.as_view(), name="logout"),
]
