from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from accounts.models import Profile

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

def add_post(request):
    if request.method == "POST":
        pass
    else:
        return render(request, "pics/add_post.html")