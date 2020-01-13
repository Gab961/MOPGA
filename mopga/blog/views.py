from django.shortcuts import render,get_object_or_404
from django.http import Http404

from .models import Projet
from .forms import ProjetForm

def home(request):
	#list = Post.objects.all()
	return render(request,'pages/home.html')

def show(request, id):
	#article = get_object_or_404(Post,pk=id)

	return render(request, 'pages/show.html')

def newProject(request):
	

	if request.method == 'POST':
		form = ProjetForm(request.POST)
		if form.is_valid():
			pass				
			#form.save()

	else:
		form=ProjetForm()


	return render(request, 'pages/newProject.html',{'form': form})


def handler404(request,exception):
	return render(request, 'errors/404.html',{'error':exception}, status=400)
