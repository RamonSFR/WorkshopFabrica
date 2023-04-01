from django.db import models

class Loja(models.Model):
    nome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=30)
    preco = models.DecimalField(max_digits=10,decimal_places=5)
    categoria = models.CharField(max_length=20)
    estoque = models.IntegerField()

    def __str__(self):
        return self.nome
    
class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=12)
    cpf = models.CharField(max_length=13)

    def __str__(self):
        return self.nome
    
