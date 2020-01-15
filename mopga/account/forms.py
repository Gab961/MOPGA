from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import Utilisateur

class UserSignUpForm(UserCreationForm):
    class Meta:
        model = Utilisateur
        fields = ('username','address','email','password1','password2')


class UserSignInForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Utilisateur
        fields = ('username','password')
