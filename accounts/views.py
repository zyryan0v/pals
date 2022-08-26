from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from .forms import LoginForm, RegistrationForm

def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            return render(request, "accounts/sign_up.html", {
                "form": form, 
            })
    else:
        form = RegistrationForm
        return render(request, "accounts/sign_up.html", {
            "form": form, 
        })

def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")
        else:
            return render(request, "accounts/login.html", {
                "form": form, 
            })

    else:
        form = LoginForm
        return render(request, "accounts/login.html", {
            "form": form, 
        })

class UserLogoutView(LogoutView):
    template_name = "accounts/logged_out.html"

