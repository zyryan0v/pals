from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField("Image")
    desc = models.CharField("Description", max_length=500, blank=True)

    def __str__(self):
        return self.img.name