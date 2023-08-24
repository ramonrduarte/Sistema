from .models import Pedido
from django.views.generic.edit import CreateView
from django.http import JsonResponse
from django.views import View
from .models import Perfil, PerfilPuxador, DivisoriaAmbiente, Acabamento, Vidro
from cadastros.models import ModeloVidro
from django.shortcuts import get_object_or_404

class PedidoCreate(CreateView):
    model = Pedido
    fields = '__all__'
    template_name = 'Pedidos/orcamento.html'

    def get_perfil_puxadores(self, request):
        perfil_id = request.GET.get('perfil_id')
        perfil = Perfil.objects.get(id=perfil_id)
        perfil_puxadores = perfil.perfil_puxador.all()

        # Crie uma lista de dicionários com os perfis puxadores relacionados
        resultados = []
        for perfil_puxador in perfil_puxadores:
            resultados.append({
                'id': perfil_puxador.id,
                'descricao': perfil_puxador.descricao
            })

        return JsonResponse(resultados, safe=False)

class FiltrarAcabamentoView(View):
    def get(self, request):
        acabamento = request.GET.get('acabamento')

        queryset = Perfil.objects.all()

        if acabamento:
            queryset = queryset.filter(acabamento__id=acabamento)

        # Crie uma lista de dicionários com os resultados filtrados
        resultados = []
        for objeto in queryset:
            resultados.append({
                'id': objeto.id,
                'descricao': f"({objeto.codigo}) {objeto.descricao}"
            })

        return JsonResponse(resultados, safe=False)

class buscar_PerfilPuxador(View):
    def get(self, request):
        perfil_id = request.GET.get('perfil')

        perfil = get_object_or_404(Perfil, id=perfil_id)
        perfispuxadores = perfil.perfilpuxador.all()

        # Crie uma lista de dicionários com os resultados filtrados
        resultados = []
        for objeto in perfispuxadores:
            resultados.append({
                'id': objeto.id,
                'descricao': f"({objeto.codigo}) {objeto.descricao}"
            })

        return JsonResponse(resultados, safe=False)

class buscar_Puxador(View):
    def get(self, request):
        perfil_id = request.GET.get('perfil')

        perfil = get_object_or_404(Perfil, id=perfil_id)
        puxadores = perfil.puxador.all()

        # Crie uma lista de dicionários com os resultados filtrados
        resultados = []
        for objeto in puxadores:
            resultados.append({
                'id': objeto.id,
                'descricao': f"({objeto.codigo}) {objeto.descricao}"
            })

        return JsonResponse(resultados, safe=False)

class buscar_Vidro(View):
    def get(self, request):
        modelo = ModeloVidro.objects.get(modelo='4MM')
        queryset = Vidro.objects.filter(modelo=modelo)

        resultados = []
        for objeto in queryset:
            resultados.append({
                'id': objeto.id,
                'descricao': f"({objeto.codigo}) {objeto.descricao}"
            })

        return JsonResponse(resultados, safe=False)

class buscar_Divisor(View):
    def get(self, request):
        perfil_id = request.GET.get('perfil')

        perfil = get_object_or_404(Perfil, id=perfil_id)
        divisores = perfil.divisor.all()

        # Crie uma lista de dicionários com os resultados filtrados
        resultados = []
        for objeto in divisores:
            resultados.append({
                'id': objeto.id,
                'descricao': f"({objeto.codigo}) {objeto.descricao}"
            })

        return JsonResponse(resultados, safe=False)

class filtrar_divisoriaView(View):
    def get(self, request):
        acabamento = request.GET.get('acabamento')
        linha = request.GET.get('linha')

        queryset = DivisoriaAmbiente.objects.filter(posicao__in=['Superior', 'Superior/Inferior'])

        if acabamento and linha:
            queryset = queryset.filter(acabamento_id=acabamento, linha=linha)

        # Crie uma lista de dicionários com os resultados filtrados
        resultados = []
        for objeto in queryset:
            resultados.append({
                'id': objeto.id,
                'descricao': f"({objeto.codigo}) {objeto.descricao}"
            })

        return JsonResponse(resultados, safe=False)

class carregar_divinferiorView(View):
    def get(self, request):
        acabamento = request.GET.get('acabamento')
        linha = request.GET.get('linha')

        queryset = DivisoriaAmbiente.objects.filter(posicao__in=['Inferior', 'Superior/Inferior', 'Travessa/Inferior'])

        if acabamento and linha:
            queryset = queryset.filter(acabamento_id=acabamento, linha=linha)

        # Crie uma lista de dicionários com os resultados filtrados
        resultados = []
        for objeto in queryset:
            resultados.append({
                'id': objeto.id,
                'descricao': f"({objeto.codigo}) {objeto.descricao}"
            })

        return JsonResponse(resultados, safe=False)

class carregar_divlateralView(View):
    def get(self, request):
        acabamento = request.GET.get('acabamento')
        linha = request.GET.get('linha')

        queryset = DivisoriaAmbiente.objects.filter(posicao__in=['Lateral'])

        if acabamento and linha:
            queryset = queryset.filter(acabamento_id=acabamento, linha=linha)

        # Crie uma lista de dicionários com os resultados filtrados
        resultados = []
        for objeto in queryset:
            resultados.append({
                'id': objeto.id,
                'descricao': f"({objeto.codigo}) {objeto.descricao}"
            })

        return JsonResponse(resultados, safe=False)

class carregar_divdivisorView(View):
    def get(self, request):
        acabamento = request.GET.get('acabamento')
        linha = request.GET.get('linha')

        queryset = DivisoriaAmbiente.objects.filter(posicao__in=['Travessa', 'Travessa/Inferior'])

        if acabamento and linha:
            queryset = queryset.filter(acabamento_id=acabamento, linha=linha)

        # Crie uma lista de dicionários com os resultados filtrados
        resultados = []
        for objeto in queryset:
            resultados.append({
                'id': objeto.id,
                'descricao': f"({objeto.codigo}) {objeto.descricao}"
            })

        return JsonResponse(resultados, safe=False)

def obter_acabamentos_divisoria_ambiente(request):
    # Consulta ao banco de dados para obter os acabamentos selecionados na DivisoriaAmbiente
    divisoria_ambientes = DivisoriaAmbiente.objects.all()
    acabamentos = divisoria_ambientes.values_list('acabamento', flat=True).distinct()
    acabamentos = Acabamento.objects.filter(divisoriaambiente__isnull=False).distinct().values('id', 'acabamento')

    data = {
        'acabamentos': list(acabamentos)
    }

    return JsonResponse(data)

def obter_acabamentos(request):
    perfil = Perfil.objects.all()
    acabamentos = perfil.values_list('acabamento', flat=True).distinct()
    acabamentos = Acabamento.objects.filter(perfil__isnull=False).distinct().values('id', 'acabamento')

    data = {
        'acabamentos': list(acabamentos)
    }

    return JsonResponse(data)

def obter_codigo_rgb(request):
    acabamento_id = request.GET.get('acabamento_id')
    acabamento = Acabamento.objects.get(pk=acabamento_id)

    # Supondo que o modelo Acabamento possui um campo chamado "codigo_rgb"
    codigo_rgb = acabamento.codigo_rgb

    # Retornar o código RGB como resposta na requisição Ajax
    return JsonResponse({'codigo_rgb': codigo_rgb})