from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Acabamento, ModeloPerfil, ModeloPerfilPuxador, ModeloPuxador, ModeloPerfilPuxador, ModeloDivisor, ModeloDivisoriaAmbiente, ModeloVidro, Tipo, Perfil, PerfilPuxador
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render


# Create your views here.

class AcabamentoCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = Acabamento
    fields = ['acabamento']
    template_name = 'cadastros/form3.html'
    success_url = reverse_lazy('listar-acabamento')
    permission_required = 'cadastros.add.acabamento'

class ModeloPerfilCreate(CreateView):
    model = ModeloPerfil
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloPerfilPuxadorCreate(CreateView):
    model = ModeloPerfilPuxador
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloPuxadorCreate(CreateView):
    model = ModeloPuxador
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloDivisorCreate(CreateView):
    model = ModeloDivisor
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloDivisoriaAmbienteCreate(CreateView):
    model = ModeloDivisoriaAmbiente
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloVidroCreate(CreateView):
    model = ModeloVidro
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')

class TipoCreate(CreateView):
    model = Tipo
    fields = ['tipo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-tipo')

class PerfilCreate(CreateView):
    model = Perfil
    fields = ['codigo', 'descricao', 'preco', 'acabamento', 'tipo', 'modelo', 'encaixe', 'puxadorsobreposto','testando']
    template_name = 'cadastros/CadPerfil.html'
    success_url = reverse_lazy('listar-perfil')

class PerfilPuxadorCreate(CreateView):
    model = PerfilPuxador
    fields = ['codigo', 'descricao', 'preco', 'acabamento', 'tipo', 'modelo', 'perfilencaixe']
    template_name = 'cadastros/CadPerfilPuxador.html'
    success_url = reverse_lazy('listar-perfilpuxador')

##################### UPDATE #####################

class AcabamentoUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Acabamento
    fields = ['acabamento']
    template_name = 'cadastros/form3.html'
    success_url = reverse_lazy('listar-acabamento')
    permission_required = 'cadastros.change.acabamento'

class ModeloPerfilUpdate(UpdateView):
    model = ModeloPerfil
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloPerfilPuxadorUpdate(UpdateView):
    model = ModeloPerfilPuxador
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloPuxadorUpdate(UpdateView):
    model = ModeloPuxador
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloDivisorUpdate(UpdateView):
    model = ModeloDivisor
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloDivisoriaAmbienteUpdate(UpdateView):
    model = ModeloDivisoriaAmbiente
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloVidroUpdate(UpdateView):
    model = ModeloVidro
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')

class TipoUpdate(UpdateView):
    model = Tipo
    fields = ['tipo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-tipo')

class PerfilUpdate(UpdateView):
    model = Perfil
    fields = ['codigo', 'descricao', 'preco', 'acabamento', 'tipo', 'modelo', 'encaixe', 'puxadorsobreposto','testando']
    template_name = 'cadastros/CadPerfil.html'
    success_url = reverse_lazy('listar-perfil')

class PerfilPuxadorUpdate(UpdateView):
    model = PerfilPuxador
    fields = ['codigo', 'descricao', 'preco', 'acabamento', 'tipo', 'modelo', 'perfilencaixe']
    template_name = 'cadastros/CadPerfilPuxador.html'
    success_url = reverse_lazy('listar-perfilpuxador')

##################### DELETE #####################

class AcabamentoDelete(LoginRequiredMixin, PermissionRequiredMixin,DeleteView):
    model = Acabamento
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-acabamento')
    permission_required = 'cadastros.delete.acabamento'

class ModeloPerfilDelete(DeleteView):
    model = ModeloPerfil
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloPerfilPuxadorDelete(DeleteView):
    model = ModeloPerfilPuxador
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloPuxadorDelete(DeleteView):
    model = ModeloPuxador
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloDivisorDelete(DeleteView):
    model = ModeloDivisor
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloDivisoriaAmbienteDelete(DeleteView):
    model = ModeloDivisoriaAmbiente
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloVidroDelete(DeleteView):
    model = ModeloVidro
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-modelos')

class TipoDelete(DeleteView):
    model = Tipo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-tipo')

class PerfilDelete(DeleteView):
    model = Perfil
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-perfil')

class PerfilPuxadorDelete(DeleteView):
    model = PerfilPuxador
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-perfilpuxador')

##################### LISTVIEW #####################

class AcabamentoList(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    model = Acabamento
    template_name = 'cadastros/listas/acabamento.html'
    permission_required = 'cadastros.view_acabamento'

# class ModeloPerfilList(ListView):
#     model = ModeloPerfil
#     template_name = 'cadastros/listas/modeloperfil.html'
#
# class ModeloPerfilPuxadorList(ListView):
#     model = ModeloPerfilPuxador
#     template_name = 'cadastros/listas/modeloperfilpuxador.html'

class TipoList(ListView):
    model = Tipo
    template_name = 'cadastros/listas/tipo.html'

class PerfilList(ListView):
    model = Perfil
    template_name = 'cadastros/listas/perfil.html'

class PerfilPuxadorList(ListView):
    model = PerfilPuxador
    template_name = 'cadastros/listas/PerfilPuxador.html'

def Modelos (request):
    modeloperfil = ModeloPerfil.objects.all()
    modeloperfilpuxador = ModeloPerfilPuxador.objects.all()
    modelopuxador = ModeloPuxador.objects.all()
    modelodivisor = ModeloDivisor.objects.all()
    modelodivisoriaambiente = ModeloDivisoriaAmbiente.objects.all()
    modelovidro = ModeloVidro.objects.all()
    return render(request, 'cadastros/listas/modelos.html', {'modeloperfil': modeloperfil,
                                                             'modeloperfilpuxador': modeloperfilpuxador,
                                                             'modelopuxador': modelopuxador,
                                                             'modelodivisor': modelodivisor,
                                                             'modelodivisoriaambiente': modelodivisoriaambiente,
                                                             'modelovidro': modelovidro})
