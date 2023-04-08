from django.urls import path
from . import views

urlpatterns = [
    path("profile/<str:username>", views.show_profile, name="show_profile"),
    path("posts/add", views.ImageCreateView.as_view(), name="add_post")
]
