from django.db import models
from Clientes.models import Cliente
from cadastros.models import Perfil, PerfilPuxador, Puxador, Divisor, DivisoriaAmbiente, Vidro, LINHA, POSICAODIVISORIA, Acabamento
from .choices import StatusPedido, Abertura
from datetime import datetime


class Pedido(models.Model):
    numero = models.CharField(max_length=8)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    data_pedido = models.DateTimeField(default=datetime.now(), blank=True)
    status = models.CharField(max_length=10, default="Aberto", choices=StatusPedido.choices)
    quantidade = models.CharField(max_length=2)
    largura = models.CharField(max_length=4)
    altura = models.CharField(max_length=4)
    acabamento = models.ForeignKey(Acabamento, on_delete=models.SET_NULL, null=True)
    abertura = models.CharField(max_length=10, choices=Abertura.choices)
    linha = models.CharField(max_length=10, choices=LINHA, verbose_name="Linha", blank=False, null=False)
    perfil = models.ForeignKey(Perfil, on_delete=models.PROTECT, verbose_name="Perfil")
    perfilpuxador = models.ForeignKey(PerfilPuxador, on_delete=models.PROTECT, verbose_name="Perfil Puxador")
    puxador = models.ForeignKey(Puxador, on_delete=models.PROTECT, verbose_name="Puxador")
    divisor = models.ForeignKey(Divisor, on_delete=models.PROTECT, verbose_name="Divisor")
    divisoriaambiente = models.ForeignKey(DivisoriaAmbiente, on_delete=models.PROTECT, verbose_name="Divisoria de Ambiente")
    vidro = models.ForeignKey(Vidro, on_delete=models.PROTECT, verbose_name="Vidro")

    def __str__(self):
        return self.numero