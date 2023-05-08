from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Acabamento, ModeloPerfil, ModeloPerfilPuxador, ModeloPuxador, ModeloPerfilPuxador, ModeloDivisor, ModeloDivisoriaAmbiente, ModeloVidro, Tipo, Perfil, PerfilPuxador, Puxador, Divisor, DivisoriaAmbiente, Vidro
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

class ModeloPerfilCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = ModeloPerfil
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloPerfilPuxadorCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = ModeloPerfilPuxador
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloPuxadorCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = ModeloPuxador
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloDivisorCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = ModeloDivisor
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloDivisoriaAmbienteCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = ModeloDivisoriaAmbiente
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloVidroCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = ModeloVidro
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')

class TipoCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = Tipo
    fields = ['tipo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-tipo')

class PerfilCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = Perfil
    fields = ['codigo', 'descricao', 'preco', 'acabamento', 'tipo', 'modelo', 'encaixe', 'puxadorsobreposto','testando']
    template_name = 'cadastros/CadPerfil.html'
    success_url = reverse_lazy('listar-perfil')

class PerfilPuxadorCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = PerfilPuxador
    fields = ['codigo', 'descricao', 'preco', 'acabamento', 'tipo', 'modelo', 'perfilencaixe']
    template_name = 'cadastros/CadPerfilPuxador.html'
    success_url = reverse_lazy('listar-perfilpuxador')

class PuxadorCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = Puxador
    fields = ['codigo', 'descricao', 'preco', 'acabamento', 'tipo', 'modelo']
    template_name = 'cadastros/CadPuxador.html'
    success_url = reverse_lazy('listar-puxador')

class DivisorCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = Divisor
    fields = ['codigo', 'descricao', 'preco', 'acabamento', 'tipo', 'modelo']
    template_name = 'cadastros/CadDivisor.html'
    success_url = reverse_lazy('listar-divisor')

class DivisoriaAmbienteCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = DivisoriaAmbiente
    fields = ['codigo', 'descricao', 'preco', 'acabamento', 'tipo', 'modelo','linha','posicao']
    template_name = 'cadastros/CadDivisoriaAmbiente.html'
    success_url = reverse_lazy('listar-divisoriaambiente')

class VidroCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = Vidro
    fields = ['codigo', 'descricao', 'preco', 'tipo', 'modelo']
    template_name = 'cadastros/CadVidro.html'
    success_url = reverse_lazy('listar-vidro')

##################### UPDATE #####################

class AcabamentoUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Acabamento
    fields = ['acabamento']
    template_name = 'cadastros/form3.html'
    success_url = reverse_lazy('listar-acabamento')
    permission_required = 'cadastros.change.acabamento'

class ModeloPerfilUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = ModeloPerfil
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloPerfilPuxadorUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = ModeloPerfilPuxador
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloPuxadorUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = ModeloPuxador
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloDivisorUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = ModeloDivisor
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloDivisoriaAmbienteUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = ModeloDivisoriaAmbiente
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloVidroUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = ModeloVidro
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')

class TipoUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = Tipo
    fields = ['tipo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-tipo')

class PerfilUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = Perfil
    fields = ['codigo', 'descricao', 'preco', 'acabamento', 'tipo', 'modelo', 'encaixe', 'puxadorsobreposto','testando']
    template_name = 'cadastros/CadPerfil.html'
    success_url = reverse_lazy('listar-perfil')

class PerfilPuxadorUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = PerfilPuxador
    fields = ['codigo', 'descricao', 'preco', 'acabamento', 'tipo', 'modelo', 'perfilencaixe']
    template_name = 'cadastros/CadPerfilPuxador.html'
    success_url = reverse_lazy('listar-perfilpuxador')

class PuxadorUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = Puxador
    fields = ['codigo', 'descricao', 'preco', 'acabamento', 'tipo', 'modelo']
    template_name = 'cadastros/CadPuxador.html'
    success_url = reverse_lazy('listar-puxador')

class DivisorUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = Divisor
    fields = ['codigo', 'descricao', 'preco', 'acabamento', 'tipo', 'modelo']
    template_name = 'cadastros/CadDivisor.html'
    success_url = reverse_lazy('listar-divisor')

class DivisoriaAmbienteUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = DivisoriaAmbiente
    fields = ['codigo', 'descricao', 'preco', 'acabamento', 'tipo', 'modelo','linha','posicao']
    template_name = 'cadastros/CadDivisoriaAmbiente.html'
    success_url = reverse_lazy('listar-divisoriaambiente')

class VidroUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = Vidro
    fields = ['codigo', 'descricao', 'preco', 'tipo', 'modelo']
    template_name = 'cadastros/CadVidro.html'
    success_url = reverse_lazy('listar-vidro')

##################### DELETE #####################

class AcabamentoDelete(LoginRequiredMixin, PermissionRequiredMixin,DeleteView):
    model = Acabamento
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-acabamento')
    permission_required = 'cadastros.delete.acabamento'

class ModeloPerfilDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = ModeloPerfil
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloPerfilPuxadorDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = ModeloPerfilPuxador
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloPuxadorDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = ModeloPuxador
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloDivisorDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = ModeloDivisor
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloDivisoriaAmbienteDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = ModeloDivisoriaAmbiente
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-modelos')

class ModeloVidroDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = ModeloVidro
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-modelos')

class TipoDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = Tipo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-tipo')

class PerfilDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = Perfil
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-perfil')

class PerfilPuxadorDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = PerfilPuxador
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-perfilpuxador')

class PuxadorDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = Puxador
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-puxador')

class DivisorDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = Divisor
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-divisor')

class DivisoriaAmbienteDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = DivisoriaAmbiente
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-divisoriaambiente')

class VidroDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = Vidro
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-vidro')

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

class TipoList(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    model = Tipo
    template_name = 'cadastros/listas/tipo.html'

class PerfilList(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    model = Perfil
    template_name = 'cadastros/listas/perfil.html'

class PerfilPuxadorList(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    model = PerfilPuxador
    template_name = 'cadastros/listas/PerfilPuxador.html'

class PuxadorList(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    model = Puxador
    template_name = 'cadastros/listas/Puxador.html'

class DivisorList(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    model = Divisor
    template_name = 'cadastros/listas/Divisor.html'

class DivisoriaAmbienteList(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    model = DivisoriaAmbiente
    template_name = 'cadastros/listas/DivisoriaAmbiente.html'

class VidroList(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    model = Vidro
    template_name = 'cadastros/listas/Vidro.html'

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
