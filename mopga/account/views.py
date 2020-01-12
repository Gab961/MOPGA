from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('pages/home.html')

    else:
        form = AuthenticationForm()

    return render(request,'account/pages/signin.html',{'form':form})
