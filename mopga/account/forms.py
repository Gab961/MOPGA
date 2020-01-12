from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class UtilisateurForm(UserCreationForm):
    createur = forms.BooleanField()
    financeur = forms.BooleanField()
    juge = forms.BooleanField()

    class Meta:
        model = User
        fields = ["username", "createur","financeur","juge","password1","password2"]
