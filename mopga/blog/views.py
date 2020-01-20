from django.shortcuts import render,get_object_or_404,redirect
from django.http import Http404

from account.models import User
from .models import Projet, Note, moneyGiven
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
		moneyGiven.objects.create(
			idProject = id,
			financeur = request.user.username,
			moneyGiven= moneyToAdd,
			)

		return redirect("show",id=id)

	if request.method == 'POST' and 'note-btn' in request.POST:
		note=request.POST.get('note')
		idProjet = id
		expert = request.user.username
		commentaire=request.POST.get('comment')
		query = Note.objects.filter(idProject=id,expert=expert)
		if query.count() == 0:
			Note.objects.create(
				idProject = idProjet,
		    	expert = expert,
		    	note=note,
				comment=commentaire
				)


	querysets = Note.objects.filter(idProject=id)
	sum = 0
	nb = 0
	for query in querysets:
		sum = sum + query.note
		nb = nb + 1

	note_final = 0
	if nb != 0:
		note_final = sum/nb

	querymoney = moneyGiven.objects.filter(idProject=id)
	sum = 0
	for query in querymoney:
		sum = sum + query.moneyGiven
	Projet.objects.filter(pk=id).update(budget_en_cours=sum)

	projet = get_object_or_404(Projet,pk=id)

	addMoney = addMoneyForm()
	noteForm=NoteForm()
	return render(request, 'pages/show.html',{'projet':projet,
		'addmoney':addMoney,'id':id,'NoteForm':noteForm,
		'comments':querysets,'note':note_final})

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
			image = request.FILES.get('image')
			Projet.objects.create(
			projectName = request.POST.get('projectName'),
		    description = request.POST.get('description'),
		    budget = request.POST.get('budget'),
			createur= request.user.username,
			image = image
			)
			return redirect("blog")

	else:
		form=ProjetForm()


	return render(request, 'pages/newProject.html',{'form': form})


def handler404(request,exception):
	return render(request, 'errors/404.html',{'error':exception}, status=400)
