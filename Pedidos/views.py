from .models import Pedido
from django.views.generic.edit import CreateView
from django.http import JsonResponse
from django.views import View
from .models import Perfil, Acabamento, Vidro
from cadastros.models import ModeloVidro
from django.shortcuts import get_object_or_404
# from .serializers import ModeloPerfilSerializer
from .serializers import PerfilSerializer, PerfilPuxadorSerializer, PuxadorSerializer, VidroSerializer, DivisorSerializer


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


class BaseBuscarView(View):
    model = None
    serializer_class = None

    def get_queryset(self, **kwargs):
        raise NotImplementedError("Subclasses of BaseBuscarView must provide a get_queryset method.")

    def serialize_data(self, queryset):
        serialized_data = self.serializer_class(queryset, many=True).data
        return serialized_data

    def get(self, request, *args, **kwargs):
        data = self.request.GET
        queryset = self.get_queryset(**data)

        serialized_data = self.serialize_data(queryset)

        return JsonResponse(serialized_data, safe=False)


class BuscarPerfil(View):
    def get(self, request):
        acabamento = request.GET.get('acabamento')

        queryset = Perfil.objects.all()

        if acabamento:
            queryset = queryset.filter(acabamento__id=acabamento)

        serializer = PerfilSerializer(queryset, many=True)

        return JsonResponse(serializer.data, safe=False)


# class BuscarPerfil(View):
#     def get(self, request):
#         acabamento = request.GET.get('acabamento')
#
#         queryset = Perfil.objects.all()
#
#         # Inicialize serialized_data fora do bloco condicional
#         serialized_data = []
#
#         if acabamento:
#             queryset = queryset.filter(acabamento__id=acabamento)
#
#             # Serialize os objetos usando o serializer
#             serializer = ModeloPerfilSerializer(queryset, many=True)
#             serialized_data = serializer.data
#
#         return JsonResponse(serialized_data, safe=False)


# class BuscarPerfilPuxador(View):
#     def get(self, request):
#         perfil_id = request.GET.get('perfil')
#
#         perfil = get_object_or_404(Perfil, id=perfil_id)
#         perfispuxadores = perfil.perfilpuxador.all()
#
#         # Crie uma lista de dicionários com os resultados filtrados
#         resultados = []
#         for objeto in perfispuxadores:
#             resultados.append({
#                 'id': objeto.id,
#                 'descricao': f"({objeto.codigo}) {objeto.descricao}",
#             })
#
#         return JsonResponse(resultados, safe=False)

class BuscarPerfilPuxador(View):
    def get(self, request):
        perfil_id = request.GET.get('perfil')

        perfil = get_object_or_404(Perfil, id=perfil_id)
        perfispuxadores = perfil.perfilpuxador.all()

        serializer = PerfilPuxadorSerializer(perfispuxadores, many=True)

        return JsonResponse(serializer.data, safe=False)


class BuscarPuxador(View):
    def get(self, request):
        perfil_id = request.GET.get('perfil')

        perfil = get_object_or_404(Perfil, id=perfil_id)
        puxadores = perfil.puxador.all()

        serializer = PuxadorSerializer(puxadores, many=True)

        return JsonResponse(serializer.data, safe=False)


class BuscarVidro(View):
    def get(self, request):
        modelo = ModeloVidro.objects.get(modelo='4MM')
        queryset = Vidro.objects.filter(modelo=modelo)

        serializer = VidroSerializer(queryset, many=True)

        return JsonResponse(serializer.data, safe=False)


class BuscarDivisor(View):
    def get(self, request):
        perfil_id = request.GET.get('perfil')

        perfil = get_object_or_404(Perfil, id=perfil_id)
        divisores = perfil.divisor.all()

        serializer = DivisorSerializer(divisores, many=True)

        return JsonResponse(serializer.data, safe=False)


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
