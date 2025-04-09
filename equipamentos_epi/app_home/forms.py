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
        fields = ['equipamento', 'colaborador', 'status','condicao_quipamento','observacao','data_devolucao','data_emprestimo','data_prevista_da_devolucao']
      
    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get('status')
        observacao = cleaned_data.get('observacao')
        datadevolucao = cleaned_data.get('data_devolucao')

        if status in ['devolvido', 'danificado', 'perdido']:
            if not observacao:
                self.add_error('observacao', 'Item não foi cadastrado: preencher campo observação.')
            if not datadevolucao:
                self.add_error('data_devolucao', 'Item não foi cadastrado: preencher campo data de devolução.')