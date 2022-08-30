from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True)
    bio = models.CharField(max_length=500, blank=True)
    follows = models.ManyToManyField("self", symmetrical=False, blank=True)

    def followers(self):
        return Profile.objects.filter(follows=self)

    def __str__(self):
        return self.user.username
    
