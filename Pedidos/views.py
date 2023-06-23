from .models import Pedido
from django.views.generic.edit import CreateView
from django.http import JsonResponse
from django.views import View
from .models import Perfil

class PedidoCreate(CreateView):
    model = Pedido
    fields = '__all__'
    template_name = 'Pedidos/novopedido.html'


class FiltrarAcabamentoView(View):
    def get(self, request):
        acabamento = request.GET.get('acabamento')

        queryset = Perfil.objects.all()

        if acabamento:
            queryset = queryset.filter(acabamento_id=acabamento)

        # Crie uma lista de dicionários com os resultados filtrados
        resultados = []
        for objeto in queryset:
            resultados.append({
                'id': objeto.id,
                'descricao': f"({objeto.codigo}) {objeto.descricao}"
            })

        return JsonResponse(resultados, safe=False)