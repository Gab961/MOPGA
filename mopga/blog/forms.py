from django import forms

from .models import Projet
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, Submit

class ProjetForm(forms.ModelForm):

    class Meta:
        model = Projet
        fields = ('projectName','description','budget')


'''
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(
        'title','description',
        Submit('submit','CREATE',css_class="btn-success")
        )'''

class addMoneyForm(forms.ModelForm):
    financement_en_cours = forms.IntegerField(label='Add money')
    class Meta:
        model = Projet
        fields = ('financement_en_cours',)

class NoteForm(forms.Form):
    CHOICES = (('0', 0),('1', 1),('2', 2),('3', 3),('4', 4),('5', 5))
    field = forms.ChoiceField(choices=CHOICES)
