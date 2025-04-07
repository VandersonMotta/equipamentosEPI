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
