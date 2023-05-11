from django.db import models
from Clientes.models import Cliente
from cadastros.models import Perfil, PerfilPuxador, Puxador, Divisor, DivisoriaAmbiente, Vidro
from .choices import StatusPedido
from datetime import datetime


class Pedido(models.Model):
    numero = models.CharField(max_length=8)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    data_pedido = models.DateTimeField(default=datetime.now(), blank=True)
    status = models.BooleanField(default="Aberto", choices=StatusPedido.choices)
    quantidade = models.CharField(max_length=2)
    largura = models.CharField(max_length=4)
    altura = models.CharField(max_length=4)
    acabamento = models.CharField(max_length=10)
    abertura = models.CharField(max_length=10)
