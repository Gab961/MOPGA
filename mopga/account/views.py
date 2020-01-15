from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password

from .models import Utilisateur
from .forms import UserSignUpForm, UserSignInForm

# Create your views here.

def sign(request):
    formUp = UserSignUpForm()
    formIn = UserSignInForm()

    return render(request,'account/pages/signinup.html',{'formIn':formIn,'formUp':formUp})

def deconnection(request):
    print('logged out')
    logout(request)

    return redirect('home')


def contact(request):

    return render(request,'account/pages/contacts.html')

def signup(request):
    formUp = UserSignUpForm()
    formIn = UserSignInForm()
    if request.method == 'POST':
        formUp = UserSignUpForm(request.POST)
        if formUp.is_valid():
            print('util créé')
            print(request.POST.get('password1'))
            utilisateur = Utilisateur.objects.create_user(
            username=request.POST.get('username'),
            address=request.POST.get('address'),
            email=request.POST.get('email'),
            #password=make_password(request.POST.get('password1'), salt=None, hasher='default')
            password=request.POST.get('password1')
            )
            utilisateur.save()
            login(request, utilisateur)
            return redirect("home")

    return render(request,'account/pages/signinup.html',{'formIn':formIn,'formUp':formUp})


def signin(request):
    formUp = UserSignUpForm()
    formIn = UserSignInForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect("home")

        else:
            print(None)


    return render(request,'account/pages/signinup.html',{'formIn':formIn,'formUp':formUp})
