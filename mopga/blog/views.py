from django.shortcuts import render,get_object_or_404,redirect
from django.http import Http404

from .models import Projet
from .forms import ProjetForm,addMoneyForm, NoteForm

def home(request):
	projets = Projet.objects.order_by('created_at')
	return render(request,'pages/home.html',{'projets':projets})

def blog(request):
	projets = Projet.objects.all()
	return render(request,'pages/blog.html',{'projets':projets})

def show(request, id):
	projet = get_object_or_404(Projet,pk=id)
	if request.method == 'POST' and 'add-money-btn' in request.POST:
		moneyToAdd = request.POST.get('financement_en_cours')
		budgettmp = projet.budget_en_cours + int(moneyToAdd)
		#setattr(Projet, 'budget_en_cours', projet.budget_en_cours)
		Projet.objects.filter(pk=id).update(budget_en_cours=budgettmp)
		return redirect("show",id=id)

	projet = get_object_or_404(Projet,pk=id)
	addMoney = addMoneyForm()
	noteForm=NoteForm()
	return render(request, 'pages/show.html',{'projet':projet,'addmoney':addMoney,'id':id,'NoteForm':noteForm})

def archive(request):
	queryset = None
	if request.method == 'POST':
		queryset = Projet.objects.filter(projectName__contains =request.POST['search'])
		#queryset = Projet.objects.filter(projectName__startswith=request.POST['search'])


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
