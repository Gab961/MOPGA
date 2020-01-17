from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


from .models import Contact, User

class UserSignUpForm(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255,required=False)
    image = forms.ImageField(required=False)
    address = forms.CharField(max_length=255,required=False)
    creator = forms.BooleanField(required=False)
    expert = forms.BooleanField(required=False)
    financer = forms.BooleanField(required=False)
    password1 = forms.CharField(max_length=255,widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=255,widget=forms.PasswordInput)

class UserSignInForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255,widget=forms.PasswordInput)

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Votre nom :"
        self.fields['contact_email'].label = "Votre adresse de messagerie :"
        self.fields['content'].label = "Veuillez saisir votre message :"

    class Meta:
        model = Contact
        fields = ('destination','subject','message')
