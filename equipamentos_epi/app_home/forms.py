from django import forms
from .models import Colaborador
from .models import EPI
from .models import Registrar

class ColaboradorForm(forms.ModelForm):
    class Meta: 
        model = Colaborador
        fields = ['nome', 'email', 'cargo', 'telefone']

class EPIForm(forms.ModelForm):
    class Meta:
        model = EPI
        fields = ['nomeEPI', 'descricao', 'validade', 'quantidade_disponivel', 'codigo']
 
class RegistrarForm (forms.ModelForm):
    class Meta:
        model = Registrar
        fields = ['equipamento', 'colaborador', 'status','condquipamento','observacao','datadevolucao','dataemprestimo','dataprevistadadevolucao']