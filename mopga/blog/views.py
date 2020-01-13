from django.shortcuts import render,get_object_or_404
from django.http import Http404

from .models import Projet
from .forms import ProjetForm

def home(request):
	projets = Projet.objects.all()
	return render(request,'pages/home.html',{'projets':projets})

def show(request, id):
	projet = get_object_or_404(Projet,pk=id)

	return render(request, 'pages/show.html',{'projet',projet})

def newProject(request):

	if request.method == 'POST':
		form = ProjetForm(request.POST)
		if form.is_valid():
			form=ProjetForm()
			form.save()

	else:
		form=ProjetForm()


	return render(request, 'pages/newProject.html',{'form': form})


def handler404(request,exception):
	return render(request, 'errors/404.html',{'error':exception}, status=400)
