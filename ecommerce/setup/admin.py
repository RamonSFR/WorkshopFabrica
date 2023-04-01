from django.contrib import admin
from .models import Loja,Cliente,Produto

class LojaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco')

admin.site.register(Loja, LojaAdmin)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco','categoria','estoque')

admin.site.register(Produto, ProdutoAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf','telefone')

admin.site.register(Cliente, ClienteAdmin)
