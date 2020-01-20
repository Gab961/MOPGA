from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.shortcuts import redirect

from blog.models import Projet,Note,moneyGiven

from django.template.loader import get_template
from .models import User
from .forms import UserSignUpForm, UserSignInForm, ContactForm


# Create your views here.

def sign(request):
    formUp = UserSignUpForm()
    formIn = UserSignInForm()

    return render(request, 'account/pages/signinup.html', {'formIn': formIn, 'formUp': formUp})


def deconnection(request):
    print('logged out')
    logout(request)

    return redirect('home')

def contact(request):
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
                , '')
            contact_email = request.POST.get(
                'contact_email'
                , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('account/contact_template.txt')
        context = {
            'contact_name': contact_name,
            'contact_email': contact_email,
            'form_content': form_content,
        }
        content = template.render(context)

        email = EmailMessage("New contact form submission", content,"Your website" + '', ['youremail@gmail.com'], headers={'Reply-To': contact_email})
        email.send()
        return redirect('contact')
    return render(request, 'account/pages/contacts.html', {'form': form_class, })


def signup(request):
    formUp = UserSignUpForm()
    formIn = UserSignInForm()
    if request.method == 'POST':
        formUp = UserSignUpForm(request.POST)
        if formUp.is_valid():
            creator2 = False
            if request.POST.get('creator') == 'on':
                creator2 = True
            expert2 = False
            if request.POST.get('expert') == 'on':
                expert2 = True
            financer2 = False
            if request.POST.get('financer') == 'on':
                financer2 = True

            if request.POST.get('password1') != request.POST.get('password2'):
                return render(request, 'account/pages/signinup.html', {'formIn': formIn, 'formUp': formUp})

            utilisateur = User.objects.create_user(
                username=request.POST.get('username'),
                address=request.POST.get('address'),
                image=request.FILES.get('image'),
                email=request.POST.get('email'),
                # password=make_password(request.POST.get('password1'), salt=None, hasher='default')
                password=request.POST.get('password1'),
                creator=creator2,
                expert=expert2,
                financer=financer2,
            )
            login(request, utilisateur)
            return redirect("home")

    return render(request, 'account/pages/signinup.html', {'formIn': formIn, 'formUp': formUp})


def signin(request):
    formUp = UserSignUpForm()
    formIn = UserSignInForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")

        else:
            print(None)

    return render(request, 'account/pages/signinup.html', {'formIn': formIn, 'formUp': formUp})



def profile(request,username):
    profil = User.objects.get(username=username)
    project = Projet.objects.filter(createur=username)
    financed = moneyGiven.objects.filter(financeur=username)
    judged = Note.objects.filter(expert=username)

    return render(request, 'account/pages/profile.html',{'profil':profil,
    'project':project,'financed':financed,'judged':judged})
