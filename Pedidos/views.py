from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class PedidoCreate(CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'paginas/orcamento.html'
