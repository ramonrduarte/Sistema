from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Acabamento, ModeloPerfil, ModeloPerfilPuxador, ModeloPuxador, ModeloPerfilPuxador, ModeloDivisor, ModeloDivisoriaAmbiente, ModeloVidro, Tipo, Perfil, PerfilPuxador, Puxador, Divisor, DivisoriaAmbiente, Vidro
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render


# Create your views here.

class AcabamentoCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Acabamento
    fields = ['acabamento']
    template_name = 'cadastros/form3.html'
    success_url = reverse_lazy('listar-acabamento')
    permission_required = 'cadastros.add.acabamento'

class ModeloPerfilCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = ModeloPerfil
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')
    permission_required = 'cadastros.add.modeloperfil'

class ModeloPerfilPuxadorCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = ModeloPerfilPuxador
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')
    permission_required = 'cadastros.add.modeloperfilpuxador'


class ModeloPuxadorCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = ModeloPuxador
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')
    permission_required = 'cadastros.add.modelopuxador'

class ModeloDivisorCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = ModeloDivisor
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')
    permission_required = 'cadastros.add.modelodivisor'

class ModeloDivisoriaAmbienteCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = ModeloDivisoriaAmbiente
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')
    permission_required = 'cadastros.add.modelodivisoriaambiente'

class ModeloVidroCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = ModeloVidro
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')
    permission_required = 'cadastros.add.modelovidro'

class TipoCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Tipo
    fields = ['tipo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-tipo')
    permission_required = 'cadastros.add.tipo'

class PerfilCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = Perfil
    fields = ['codigo', 'descricao', 'preco', 'acabamento', 'tipo', 'modelo', 'encaixe', 'puxadorsobreposto','testando']
    template_name = 'cadastros/CadPerfil.html'
    success_url = reverse_lazy('listar-perfil')
    permission_required = 'cadastros.add.perfil'

class PerfilPuxadorCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = PerfilPuxador
    fields = ['codigo', 'descricao', 'preco', 'acabamento', 'tipo', 'modelo', 'perfilencaixe']
    template_name = 'cadastros/CadPerfilPuxador.html'
    success_url = reverse_lazy('listar-perfilpuxador')
    permission_required = 'cadastros.add.perfilpuxador'

class PuxadorCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = Puxador
    fields = ['codigo', 'descricao', 'preco', 'acabamento', 'tipo', 'modelo']
    template_name = 'cadastros/CadPuxador.html'
    success_url = reverse_lazy('listar-puxador')
    permission_required = 'cadastros.add.puxador'

class DivisorCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = Divisor
    fields = ['codigo', 'descricao', 'preco', 'acabamento', 'tipo', 'modelo']
    template_name = 'cadastros/CadDivisor.html'
    success_url = reverse_lazy('listar-divisor')
    permission_required = 'cadastros.add.divisor'

class DivisoriaAmbienteCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = DivisoriaAmbiente
    fields = ['codigo', 'descricao', 'preco', 'acabamento', 'tipo', 'modelo','linha','posicao']
    template_name = 'cadastros/CadDivisoriaAmbiente.html'
    success_url = reverse_lazy('listar-divisoriaambiente')
    permission_required = 'cadastros.add.divisoriaambiente'

class VidroCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = Vidro
    fields = ['codigo', 'descricao', 'preco', 'tipo', 'modelo']
    template_name = 'cadastros/CadVidro.html'
    success_url = reverse_lazy('listar-vidro')
    permission_required = 'cadastros.add.vidro'

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
    permission_required = 'cadastros.change.modeloperfil'

class ModeloPerfilPuxadorUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = ModeloPerfilPuxador
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')
    permission_required = 'cadastros.change.modeloperfilpuxador'

class ModeloPuxadorUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = ModeloPuxador
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')
    permission_required = 'cadastros.change.modelopuxador'

class ModeloDivisorUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = ModeloDivisor
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')
    permission_required = 'cadastros.change.modelodivisor'

class ModeloDivisoriaAmbienteUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = ModeloDivisoriaAmbiente
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')
    permission_required = 'cadastros.change.modelodivisoriaambiente'

class ModeloVidroUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = ModeloVidro
    fields = ['modelo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelos')
    permission_required = 'cadastros.change.modelovidro'

class TipoUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = Tipo
    fields = ['tipo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-tipo')
    permission_required = 'cadastros.change.tipo'

class PerfilUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = Perfil
    fields = ['codigo', 'descricao', 'preco', 'acabamento', 'tipo', 'modelo', 'encaixe', 'puxadorsobreposto','testando']
    template_name = 'cadastros/CadPerfil.html'
    success_url = reverse_lazy('listar-perfil')
    permission_required = 'cadastros.change.perfil'

class PerfilPuxadorUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = PerfilPuxador
    fields = ['codigo', 'descricao', 'preco', 'acabamento', 'tipo', 'modelo', 'perfilencaixe']
    template_name = 'cadastros/CadPerfilPuxador.html'
    success_url = reverse_lazy('listar-perfilpuxador')
    permission_required = 'cadastros.change.perfilpuxador'

class PuxadorUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = Puxador
    fields = ['codigo', 'descricao', 'preco', 'acabamento', 'tipo', 'modelo']
    template_name = 'cadastros/CadPuxador.html'
    success_url = reverse_lazy('listar-puxador')
    permission_required = 'cadastros.change.puxador'

class DivisorUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = Divisor
    fields = ['codigo', 'descricao', 'preco', 'acabamento', 'tipo', 'modelo']
    template_name = 'cadastros/CadDivisor.html'
    success_url = reverse_lazy('listar-divisor')
    permission_required = 'cadastros.change.divisor'

class DivisoriaAmbienteUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = DivisoriaAmbiente
    fields = ['codigo', 'descricao', 'preco', 'acabamento', 'tipo', 'modelo','linha','posicao']
    template_name = 'cadastros/CadDivisoriaAmbiente.html'
    success_url = reverse_lazy('listar-divisoriaambiente')
    permission_required = 'cadastros.change.divisoriaambiente'

class VidroUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = Vidro
    fields = ['codigo', 'descricao', 'preco', 'tipo', 'modelo']
    template_name = 'cadastros/CadVidro.html'
    success_url = reverse_lazy('listar-vidro')
    permission_required = 'cadastros.change.vidro'

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
    permission_required = 'cadastros.delete.modeloperfil'

class ModeloPerfilPuxadorDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = ModeloPerfilPuxador
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-modelos')
    permission_required = 'cadastros.delete.modeloperfilpuxador'

class ModeloPuxadorDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = ModeloPuxador
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-modelos')
    permission_required = 'cadastros.delete.modelopuxador'

class ModeloDivisorDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = ModeloDivisor
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-modelos')
    permission_required = 'cadastros.delete.modelodivisor'

class ModeloDivisoriaAmbienteDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = ModeloDivisoriaAmbiente
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-modelos')
    permission_required = 'cadastros.delete.modelodivisoriaambiente'

class ModeloVidroDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = ModeloVidro
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-modelos')
    permission_required = 'cadastros.delete.modelovidro'

class TipoDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = Tipo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-tipo')
    permission_required = 'cadastros.delete.tipo'

class PerfilDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = Perfil
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-perfil')
    permission_required = 'cadastros.delete.perfil'

class PerfilPuxadorDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = PerfilPuxador
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-perfilpuxador')
    permission_required = 'cadastros.delete.perfilpuxador'

class PuxadorDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = Puxador
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-puxador')
    permission_required = 'cadastros.delete.puxador'

class DivisorDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = Divisor
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-divisor')
    permission_required = 'cadastros.delete.divisoria'

class DivisoriaAmbienteDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = DivisoriaAmbiente
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-divisoriaambiente')
    permission_required = 'cadastros.delete.divisoriaambiente'

class VidroDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = Vidro
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-vidro')
    permission_required = 'cadastros.delete.vidro'

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

class TipoList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Tipo
    template_name = 'cadastros/listas/tipo.html'
    permission_required = 'cadastros.view.tipo'

class PerfilList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Perfil
    template_name = 'cadastros/listas/perfil.html'
    permission_required = 'cadastros.view_perfil'


class PerfilPuxadorList(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    model = PerfilPuxador
    template_name = 'cadastros/listas/PerfilPuxador.html'
    permission_required = 'cadastros.view_perfilpuxador'

class PuxadorList(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    model = Puxador
    template_name = 'cadastros/listas/Puxador.html'
    permission_required = 'cadastros.view_puxador'

class DivisorList(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    model = Divisor
    template_name = 'cadastros/listas/Divisor.html'
    permission_required = 'cadastros.view_divisor'

class DivisoriaAmbienteList(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    model = DivisoriaAmbiente
    template_name = 'cadastros/listas/DivisoriaAmbiente.html'
    permission_required = 'cadastros.view_divisoriaambiente'

class VidroList(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    model = Vidro
    template_name = 'cadastros/listas/Vidro.html'
    permission_required = 'cadastros.view_vidro'

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
