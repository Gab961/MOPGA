from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required

from .models import User
from .forms import UserSignUpForm, UserSignInForm, ContactForm

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
    contact = ContactForm()
    return render(request,'account/pages/contacts.html',{'contact':contact})


def signup(request):
    formUp = UserSignUpForm()
    formIn = UserSignInForm()
    if request.method == 'POST':
        formUp = UserSignUpForm(request.POST)
        if formUp.is_valid():
            creator2=False
            if request.POST.get('creator')=='on':
                creator2 = True
            expert2=False
            if request.POST.get('expert')=='on':
                expert2 = True
            financer2=False
            if request.POST.get('financer')=='on':
                financer2 = True

            if request.POST.get('password1') != request.POST.get('password2'):
                return

            utilisateur = User.objects.create_user(
            username=request.POST.get('username'),
            address=request.POST.get('address'),
            email=request.POST.get('email'),
            image=request.POST.get('image'),
            #password=make_password(request.POST.get('password1'), salt=None, hasher='default')
            password=request.POST.get('password1'),
            creator=creator2,
            expert=expert2,
            financer=financer2,
            )
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


@login_required
def profile(request):
    return render(request, 'account/pages/profile.html')
