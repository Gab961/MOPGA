from django.shortcuts import render,get_object_or_404
from django.http import Http404

from .models import Post
from .forms import PostForm

def home(request):
	list = Post.objects.all()
	return render(request,'pages/home.html',{'posts':list})

def show(request, id):
	article = get_object_or_404(Post,pk=id)

	return render(request, 'pages/show.html', {'post':article})

def newProject(request):

	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():

			title = form.cleaned_data['title']
			description = form.cleaned_data['description']

			form.save()

	else:
		form=PostForm()


	form = PostForm()
	return render(request, 'pages/newProject.html',{'form': form})


def handler404(request,exception):
	return render(request, 'errors/404.html',{'error':exception}, status=400)
