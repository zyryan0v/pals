from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import Profile
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    pass

class RegistrationForm(UserCreationForm):
    pass

class UserForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["user"]
        widgets = {
            'bio': forms.Textarea(attrs={"rows": 4}),
        }
