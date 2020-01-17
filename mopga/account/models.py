from django.db import models
from django.contrib.auth.models import AbstractUser

from blog.models import Note

# Create your models here.

LICENSES = [('CC', 'CC'),
            ('libre droit', 'libre droit'),
            ('tous droits réservés', 'tous droits réservés'),
            ]


class Image(models.Model):
    image = models.ImageField(default='default.jpg',upload_to='image_pics')
    license = models.CharField(max_length=50, choices=LICENSES)



class User(AbstractUser):
    #user = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    image = models.ImageField(default='default.png',upload_to='utilisateur_pics')
    address = models.CharField(max_length=255,blank=True)
    creator = models.BooleanField(default=False)
    expert = models.BooleanField(default=False)
    financer = models.BooleanField(default=False)
    #file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='files')

    @classmethod
    def showNote(self,id):
        query = Note.objects.filter(idProject=id,expert=self.username)
        if query.count() == 0:
            return True
        else:
            return False

class Contact(models.Model):
    destination = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=1000000000,blank=True)
