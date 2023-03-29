from django.db import models

# Create your models here.

class jogo(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=7,decimal_places=2)

    def __str__(self):
        return self.nome

class loja(models.Model):
    nome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=70)
    telefone = models.CharField(max_length=11)
    
    def __str__(self):
        return self.nome
