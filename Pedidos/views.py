from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Pedido
# from .forms import PedidoForm


class PedidoCreate(CreateView):
    model = Pedido
    fields = "__all__"
    template_name = 'Pedidos/novopedido.html'