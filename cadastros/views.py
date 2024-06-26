from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Acabamento, ModeloPerfil, ModeloPerfilPuxador, ModeloPuxador, ModeloPerfilPuxador, ModeloDivisor, ModeloDivisoriaAmbiente, ModeloVidro, Tipo, Perfil, PerfilPuxador, Puxador, Divisor, DivisoriaAmbiente, Vidro
from django.views.generic.list import ListView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from .forms import PerfilForm
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET



# Create your views here.

class AcabamentoCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Acabamento
    fields = ['acabamento', 'codigo_rgb']
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

class PerfilCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Perfil
    form_class = PerfilForm
    template_name = 'cadastros/CadPerfil.html'
    success_url = reverse_lazy('listar-perfil')
    permission_required = 'cadastros.add.perfil'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['acabamentos'] = Acabamento.objects.all()  # Passando os acabamentos para o contexto
        context['tipos'] = Tipo.objects.all()  # Passando os tipos para o contexto
        context['modelo'] = ModeloPerfil.objects.all()  # Passando os modelos para o contexto
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Defina o valor inicial do campo 'encaixe' como "2" (não)
        kwargs['initial'] = {'encaixe': '2', 'encaixedivisor': '2', 'encaixepuxador': '2'}
        return kwargs

    def form_valid(self, form):
        perfil = form.save(commit=False)
        perfil.save()
        print(perfil)
        return super().form_valid(form)



class PerfilPuxadorCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = PerfilPuxador
    fields = '__all__'
    template_name = 'cadastros/CadPerfilPuxador.html'
    success_url = reverse_lazy('listar-perfilpuxador')
    permission_required = 'cadastros.add.perfilpuxador'

class PuxadorCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = Puxador
    fields = ['codigo', 'descricao', 'preco', 'acabamento', 'tipo', 'modelo', 'desconto_puxador', 'ativo']
    template_name = 'cadastros/CadPuxador.html'
    success_url = reverse_lazy('listar-puxador')
    permission_required = 'cadastros.add.puxador'


class DivisorCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = Divisor
    fields = ['codigo', 'descricao', 'preco', 'acabamento', 'tipo', 'modelo', 'tipodivisor', 'espdivisor', 'ativo']
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
    fields = ['codigo', 'descricao', 'preco', 'tipo', 'modelo', 'ativo']
    template_name = 'cadastros/CadVidro.html'
    success_url = reverse_lazy('listar-vidro')
    permission_required = 'cadastros.add.vidro'

##################### UPDATE #####################

class AcabamentoUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Acabamento
    fields = ['acabamento', 'codigo_rgb']
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

class PerfilUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Perfil
    form_class = PerfilForm
    template_name = 'cadastros/CadPerfil.html'
    success_url = reverse_lazy('listar-perfil')
    permission_required = 'cadastros.change.perfil'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        instance = self.get_object()
        kwargs['initial'] = {'encaixe': instance.encaixe, 'encaixedivisor': instance.encaixedivisor, 'encaixepuxador': instance.encaixepuxador}
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        perfil = self.get_object()
        context['perfilpuxador_ids'] = perfil.perfilpuxador.values_list('id',flat=True)
        context['divisor_ids'] = perfil.divisor.values_list('id', flat=True)
        context['puxador_ids'] = perfil.puxador.values_list('id', flat=True)
        context['perfilpuxador'] = PerfilPuxador.objects.filter(acabamento=perfil.acabamento)
        context['divisor'] = Divisor.objects.filter(acabamento=perfil.acabamento)
        context['puxador'] = Puxador.objects.filter(acabamento=perfil.acabamento)
        context['acabamentos'] = Acabamento.objects.all()
        return context


class PerfilPuxadorUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = PerfilPuxador
    fields = '__all__'
    template_name = 'cadastros/CadPerfilPuxador.html'
    success_url = reverse_lazy('listar-perfilpuxador')
    permission_required = 'cadastros.change.perfilpuxador'

class PuxadorUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = Puxador
    fields = ['codigo', 'descricao', 'preco', 'acabamento', 'tipo', 'modelo', 'desconto_puxador', 'ativo']
    template_name = 'cadastros/CadPuxador.html'
    success_url = reverse_lazy('listar-puxador')
    permission_required = 'cadastros.change.puxador'

class DivisorUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = Divisor
    fields = ['codigo', 'descricao', 'preco', 'acabamento', 'tipo', 'modelo', 'tipodivisor', 'espdivisor', 'ativo']
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
    fields = ['codigo', 'descricao', 'preco', 'tipo', 'modelo', 'ativo']
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


class TipoList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Tipo
    template_name = 'cadastros/listas/tipo.html'
    permission_required = 'cadastros.view.tipo'

class PerfilList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Perfil
    template_name = 'cadastros/ListarPerfil.html'
    permission_required = 'cadastros.view_perfil'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['acabamentos'] = Acabamento.objects.all()  # Passando os acabamentos para o contexto
        context['tipos'] = Tipo.objects.all()  # Passando os tipos para o contexto
        context['modelo'] = ModeloPerfil.objects.all()  # Passando os modelos para o contexto

        # Obtém o perfil selecionado, se houver
        perfil_id = self.request.GET.get('perfil_id')
        perfil = None
        if perfil_id:
            perfil = get_object_or_404(Perfil, pk=perfil_id)
            context['perfil'] = perfil

            # Filtra os encaixes pelo acabamento do perfil
            context['perfilpuxador'] = PerfilPuxador.objects.filter(acabamento=perfil.acabamento)
            context['divisor'] = Divisor.objects.filter(acabamento=perfil.acabamento)
            context['puxador'] = Puxador.objects.filter(acabamento=perfil.acabamento)

            # Obtém os IDs dos encaixes selecionados
            context['perfilpuxador_ids'] = perfil.perfilpuxador.values_list('id', flat=True)
            context['divisor_ids'] = perfil.divisor.values_list('id', flat=True)
            context['puxador_ids'] = perfil.puxador.values_list('id', flat=True)

        return context


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


def filtrar_perfil(request):
    acabamento = request.GET.get('acabamento')

    queryset = PerfilPuxador.objects.all()

    if acabamento:
        queryset = queryset.filter(acabamento_id=acabamento)

    # Crie uma lista de dicionários com os resultados filtrados
    resultados = []
    for objeto in queryset:
        resultados.append({
            'id': objeto.id,
            'descricao': (f"({objeto.codigo}) {objeto.descricao}"),
        })

    return JsonResponse(resultados, safe=False)

def filtrar_divisor(request):
    acabamento = request.GET.get('acabamento')
    queryset = Divisor.objects.all()

    if acabamento:
        queryset = queryset.filter(acabamento_id=acabamento)

    # Crie uma lista de dicionários com os resultados filtrados
    resultados = []
    for objeto in queryset:
        resultados.append({
            'id': objeto.id,
            'descricao': (f"({objeto.codigo}) {objeto.descricao}"),
        })

    return JsonResponse(resultados, safe=False)

def filtrar_puxador(request):
    acabamento = request.GET.get('acabamento')
    queryset = Puxador.objects.all()

    if acabamento:
        queryset = queryset.filter(acabamento_id=acabamento)

    # Crie uma lista de dicionários com os resultados filtrados
    resultados = []
    for objeto in queryset:
        resultados.append({
            'id': objeto.id,
            'descricao': (f"({objeto.codigo}) {objeto.descricao}"),
        })

    return JsonResponse(resultados, safe=False)
