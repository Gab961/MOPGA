from django.db import models

from account.models import Utilisateur


'''
class Demandeur(models.Model):
    idRole = models.CharField(max_length=50, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')

    class Meta:
        db_table = "Demandeur"


class Expert(models.Model):
    idRole = models.CharField(max_length=50, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    karma = models.IntegerField()

    class Meta:
        db_table = "Expert"


class Financeur(models.Model):
    idRole = models.CharField(max_length=50, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    type = models.CharField(max_length=255)

    class Meta:
        db_table = "Financeur"
'''

class Projet(models.Model):
    #idProject = models.CharField(max_length=255, primary_key=True)
    projectName = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    budget = models.IntegerField()
    note = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #createur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, )
    #demandeur = models.OneToOneField(Demandeur, on_delete=models.CASCADE)
    #Expert = models.OneToOneField(Expert, on_delete=models.CASCADE)
    #Financeur = models.OneToOneField(Financeur, on_delete=models.CASCADE)
    #fichier = models.ForeignKey(File, on_delete=models.CASCADE, related_name='files')




'''
class Meta:
    db_table = "Financeur"
    db_table = "File"
    db_table = "User"
    db_table = "Demandeur"
    db_table = "Expert"
'''
