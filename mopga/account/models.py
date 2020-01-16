from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

LICENSES = [('CC', 'CC'),
            ('libre droit', 'libre droit'),
            ('tous droits réservés', 'tous droits réservés'),
            ]


class File(models.Model):
    image = models.ImageField()
    license = models.CharField(max_length=50, choices=LICENSES)

    class Meta:
        db_table = "File"


class Utilisateur(AbstractUser):
    address = models.CharField(max_length=255,blank=True)
    creator = models.BooleanField(default=False)
    expert = models.BooleanField(default=False)
    financer = models.BooleanField(default=False)
    #file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='files')

class Contact(models.Model):
    destination = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=1000000000,blank=True)
