from django.urls import path
from . import views
from django.contrib.auth import views as av

urlpatterns = [
    path("login", views.user_login, name="login"),
    path("logout", views.UserLogoutView.as_view(), name="logout"),
    path("sign-up", views.sign_up, name="sign_up"),
    path("edit", views.edit_profile, name="edit_profile"),
]
