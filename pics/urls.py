from django.urls import path
from . import views

urlpatterns = [
    path("profile/<str:username>", views.show_profile, name="show_profile"),
    path("posts/add", views.add_post, name="add_post")
]
