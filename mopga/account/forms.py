from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from .models import Contact, Utilisateur

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

class ContactForm(forms.Form):
    destination = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Contact
        fields = ('destination','subject','message')
