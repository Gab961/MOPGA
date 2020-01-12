from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UtilisateurForm

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #form.save()
            pass
        return redirect('../../')
    else:
        form = UserCreationForm()

    return render(request,'account/pages/signup.html',{'form':UtilisateurForm})


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            pass

            return redirect('../../')
    else:
        form = AuthenticationForm()

    return render(request,'account/pages/signin.html',{'form':form})
