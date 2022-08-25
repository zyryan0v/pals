from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

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

