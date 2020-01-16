from django import forms

from .models import Projet
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, Submit

class ProjetForm(forms.ModelForm):
    
    class Meta:
        model = Projet
        fields = ('projectName','description','budget','note')

'''
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(
        'title','description',
        Submit('submit','CREATE',css_class="btn-success")
        )'''

class NoteForm(forms.ModelForm):
    pass
