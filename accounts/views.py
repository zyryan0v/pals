from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
from .forms import LoginForm, RegistrationForm, ProfileForm, UserForm
from .models import Profile

@login_required
def edit_profile(request):
    user = request.user
    if request.method == "POST":

        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            
            profile_form = ProfileForm(instance=user.profile)

            messages.success(request, "Saved successfully")
            return render(request, "accounts/edit_profile.html", {
                "user_form": user_form,
                "profile_form": profile_form,
            })
        else:
            messages.error(request, "There was an error")
            return render(request, "accounts/edit_profile.html", {
                "user_form": user_form,
                "profile_form": profile_form,
            })

    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=user.profile)
        return render(request, "accounts/edit_profile.html", {
            "user_form": user_form,
            "profile_form": profile_form,
        })


def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
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
            return render(request, "accounts/sign_in.html", {
                "form": form, 
            })

    else:
        form = LoginForm
        return render(request, "accounts/sign_in.html", {
            "form": form, 
        })

class UserLogoutView(LogoutView):
    template_name = "accounts/logged_out.html"

class ChangePasswordView(PasswordChangeView):
    template_name = "accounts/change_password.html"
    success_url = reverse_lazy("change_password_done")

class ChangePasswordDoneView(PasswordChangeDoneView):
    template_name = "accounts/change_password_done.html"
