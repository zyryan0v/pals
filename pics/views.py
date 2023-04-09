from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from .models import Image
from .forms import ImageForm

def show_profile(request, username):
    display_user = get_object_or_404(User, username=username)
    profile = display_user.profile  
    images = display_user.image_set.all()
    following = profile.follows.all()
    followers = profile.followers()
    
    return render(request, "pics/profile.html", {
        "display_user": display_user,
        "profile": profile,
        "images": images,
        "following": following,
        "followers": followers,
    })

@login_required
def add_post(request):
    if request.method == "POST":
        image_form = ImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image = image_form.save(commit=False)
            image.user = request.user
            image.save()
            
            return redirect("show_profile", username=request.user.username)
        else:
            return render(request, "pics/add_post.html", {
                "form": image_form,
            })
    else:
        image_form = ImageForm()
        return render(request, "pics/add_post.html", {
            "form": image_form,
        })
    
