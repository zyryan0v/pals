from .models import Image
from django import forms

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ["user"]