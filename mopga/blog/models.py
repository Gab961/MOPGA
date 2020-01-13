from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
#from ratings.models import Rating

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	#ratings = Ratings()

	def __str__(self):
		return self.title + " : " + self.description

	def nb_of_rating(self):
		ratings = Rating.objects.filter(post=self)
		return len(ratings)


	def average_rating(self):
		sum = 0
		ratings = Rating.objects.filter(post=self)
		for rating in ratings:
			sum += rating.stars
		if len(ratings) > 0:
			return sum/len(ratings)
		else:
			return 0

class Rating(models.Model):
	post = models.ForeignKey(Post,on_delete=models.CASCADE)
	#user = models.ForeignKey(User,on_delete=models.CASCADE)
	stars = models.IntegerField(validators = [MinValueValidator(1),
		MaxValueValidator(5)])
