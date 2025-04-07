from django import forms
from .models import Colaborador
from .models import EPI

class ColaboradorForm(forms.ModelForm):
    class Meta: 
        model = Colaborador
        fields = ['nome', 'email', 'cargo', 'telefone']

class EPIForm(forms.ModelForm):
    class Meta:
        model = EPI
        fields = ['nomeEPI', 'descricao', 'validade', 'quantidade_disponivel', 'codigo']