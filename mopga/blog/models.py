from django.db import models

from account.models import Utilisateur

class Note:
    note_final = float(0)
    nb_note = 0
    notes={}

    def average(self):
        if nb_note == 0:
            note_final = 0
        else:
            self.note_final = sumTotal()/self.nb_note

    def sumTotal(self):
        sum = 0
        for key, value in self.notes.items():
            sum += value

        return sum

    def addNote(self,username,note):
        self.notes[username] = note
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
    budget = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    createur = models.CharField(max_length=255)
    financement_en_cours = models.PositiveIntegerField(default=0)
    budget_en_cours = 0
    note = Note()
    #demandeur = models.OneToOneField(Demandeur, on_delete=models.CASCADE)
    #Expert = models.OneToOneField(Expert, on_delete=models.CASCADE)
    #Financeur = models.OneToOneField(Financeur, on_delete=models.CASCADE)
    #fichier = models.ForeignKey(File, on_delete=models.CASCADE, related_name='files')

    def addCreator(self,crea):
        self.createur = crea




'''
class Meta:
    db_table = "Financeur"
    db_table = "File"
    db_table = "User"
    db_table = "Demandeur"
    db_table = "Expert"
'''
