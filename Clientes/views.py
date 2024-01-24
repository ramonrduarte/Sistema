from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cliente
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class ClientesCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Cliente
    fields = ['codigo', 'nome', 'cpf_cnpj', 'cep', 'logradouro', 'numero', 'bairro', 'cidade', 'telefone']
    template_name = 'clientes/CadClientes.html'
    success_url = reverse_lazy('listar-clientes')
    permission_required = 'Clientes.add.cliente'


class ClientesUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Cliente
    fields = ['codigo', 'nome', 'cpf_cnpj', 'cep', 'logradouro', 'numero', 'bairro', 'cidade', 'telefone']
    template_name = 'clientes/CadClientes.html'
    success_url = reverse_lazy('listar-clientes')
    permission_required = 'Clientes.change.cliente'


class ClientesDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-clientes')
    permission_required = 'Clientes.delete.cliente'


class ClientesList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Cliente
    template_name = 'clientes/novocliente.html'
    permission_required = 'Clientes.view_cliente'
