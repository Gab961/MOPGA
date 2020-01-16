from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import Utilisateur

class UserSignUpForm(UserCreationForm):
    creator = forms.BooleanField(required=False, initial=False)
    expert = forms.BooleanField(required=False, initial=False)
    financer = forms.BooleanField(required=False, initial=False)
    class Meta:
        model = Utilisateur
        fields = ('username','address','email',
        'creator','expert','financer','password1','password2')


class UserSignInForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Utilisateur
        fields = ('username','password')
