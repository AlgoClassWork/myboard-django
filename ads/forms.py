from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from ads.models import Ad

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['author', 'title', 'description', 'image']

class RegisterForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']