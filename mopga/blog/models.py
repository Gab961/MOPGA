from django.db import models

class Note(models.Model):
    idProject = models.PositiveIntegerField()
    expert = models.CharField(max_length=255)
    note = models.PositiveIntegerField()
    comment = models.CharField(max_length=10000)

class moneyGiven(models.Model):
    idProject = models.PositiveIntegerField()
    financeur = models.CharField(max_length=255)
    moneyGiven = models.PositiveIntegerField()

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
    budget_en_cours = models.PositiveIntegerField(default=0)
    createur = models.CharField(max_length=255)

    @classmethod
    def average(self):
        if self.nb_note == 0:
            self.note_final.update(self.sumTotal/self.nb_note)
        else:
            self.note_final.update(self.sumTotal/self.nb_note)

    @classmethod
    def addNote(self,note):
        self.sumTotal.update(self.sumTotal + note)
        self.nb_note.update(self.nb_note + 1)


    @classmethod
    def update(self):
        self.average()
    #demandeur = models.OneToOneField(Demandeur, on_delete=models.CASCADE)
    #Expert = models.OneToOneField(Expert, on_delete=models.CASCADE)
    #Financeur = models.OneToOneField(Financeur, on_delete=models.CASCADE)
    #fichier = models.ForeignKey(File, on_delete=models.CASCADE, related_name='files')

    @classmethod
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
