from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from accounts.models import Profile

def show_profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.profile  
    images = user.image_set.all()
    following = profile.follows.all()
    followers = profile.followers()
    
    return render(request, "pics/profile.html", {
        "user": user,
        "profile": profile,
        "images": images,
        "following": following,
        "followers": followers,
    })