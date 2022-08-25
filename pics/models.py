from django.db import models

class Image(models.Model):
    img = models.ImageField()
    desc = models.CharField(max_length=500, blank=True)
    

    def __str__(self):
        return self.img.name