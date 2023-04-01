from rest_framework import serializers
from .models import Loja,Cliente,Produto

class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = ['nome', 'endereco']

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['nome', 'preco','categoria','estoque']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'cpf']