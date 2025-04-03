from django import forms
from .models import Colaborador

class ColaboradorForm(forms.ModelForm):
    class meta: 
        model = Colaborador
        fields = ['nome', 'email', 'cargo', 'telefone']