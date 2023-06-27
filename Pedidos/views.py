from .models import Pedido
from django.views.generic.edit import CreateView
from django.http import JsonResponse
from django.views import View
from .models import Perfil, PerfilPuxador
from django.shortcuts import get_object_or_404

class PedidoCreate(CreateView):
    model = Pedido
    fields = '__all__'
    template_name = 'Pedidos/novopedido.html'

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