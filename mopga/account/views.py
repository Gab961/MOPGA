from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .forms import UserSignUpForm, UserSignInForm

# Create your views here.

def sign(request):
    formUp = UserSignUpForm()
    formIn = UserSignInForm()

    return render(request,'account/pages/signinup.html',{'formIn':formIn,'formUp':formUp})

def signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            #form.save()
            pass
            return redirect('../../')
        else:
            formUp = UserSignUpForm()
            formIn = UserSignInForm()
    else:
        formUp = UserSignUpForm()
        formIn = UserSignInForm()

    return render(request,'account/pages/signinup.html',{'formIn':formIn,'formUp':formUp})


def signin(request):
    if request.method == 'POST':
        form = UserSignInForm(data=request.POST)
        if form.is_valid():
            pass

            return redirect('../../')
        else:
            formUp = UserSignUpForm()
            formIn = UserSignInForm()
    else:
        formUp = UserSignUpForm()
        formIn = UserSignInForm()

    return render(request,'account/pages/signinup.html',{'formIn':formIn,'formUp':formUp})
