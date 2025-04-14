from django.db import models

# Create your models here.

class Colaborador(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    cargo = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class EPI(models.Model):
    nomeEPI = models.CharField(max_length=100)
    descricao = models.TextField()
    validade = models.DateField()
    quantidade_disponivel = models.IntegerField()
    codigo = models.CharField(max_length=100)

    def __str__(self):
        return self.nomeEPI
    
class Registrar(models.Model):
    STATUS_CHOICES = [
        ('emprestado', 'Emprestado'),
        ('em_uso', 'Em uso'),
        ('fornecido', 'Fornecido'),
        ('devolvido', 'Devolvido'),
        ('danificado', 'Danificado'),
        ('perdido', 'Perdido'),
    ]

    equipamento = models.ForeignKey(EPI, on_delete=models.CASCADE, related_name='registros')
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, related_name='registros')
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    condicao_equipamento = models.CharField(max_length=100)
    observacao = models.CharField(max_length=100, blank=True, null=True)
    data_devolucao = models.DateField(blank=True, null=True)
    data_emprestimo = models.DateField()
    data_prevista_da_devolucao = models.DateField()

    def __str__(self):
        return f'{self.equipamento} - {self.colaborador}'



