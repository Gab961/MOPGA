from django.db import models
from django.contrib.auth.models import User

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


class Utilisateur(User):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    #file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='files')

    class Meta:
        db_table = "Utilisateur"
