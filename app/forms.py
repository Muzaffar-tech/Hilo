from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import PasswordInput

from .models import User


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=PasswordInput())
    password2 = forms.CharField(widget=PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email')