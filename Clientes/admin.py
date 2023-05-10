from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'cpf_cnpj', 'cep', 'logradouro', 'numero', 'bairro', 'cidade', 'telefone' )