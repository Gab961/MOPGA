from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title + " : " + self.description

class User(models.Model):
	username = models.CharField(max_length=100);
	password = models.CharField(max_length=20);
	email = models.CharField(max_length=100);
	createur = models.BooleanField();
	financeur = models.BooleanField();
	juge = models.BooleanField();
