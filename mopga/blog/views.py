from django.shortcuts import render,get_object_or_404
from django.http import Http404

from .models import Projet
from .forms import ProjetForm

def home(request):
	return render(request,'pages/home.html')

def blog(request):
	projets = Projet.objects.all()
	return render(request,'pages/blog.html',{'projets':projets})

def show(request, id):
	projet = get_object_or_404(Projet,pk=id)
	return render(request, 'pages/show.html',{'projet':projet})

def archive(request):
	queryset = None
	if request.method == 'POST':
		queryset = Projet.objects.filter(projectName=request.POST['search'])


	return render(request, 'pages/archive.html',{'queryset':queryset})

def mentions(request):
	return render(request, 'pages/mentions.html')

def newProject(request):

	if request.method == 'POST':
		form = ProjetForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("blog")

	else:
		form=ProjetForm()


	return render(request, 'pages/newProject.html',{'form': form})


def handler404(request,exception):
	return render(request, 'errors/404.html',{'error':exception}, status=400)
