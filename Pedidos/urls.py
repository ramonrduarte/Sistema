from django.urls import path
from .views import PedidoCreate
from . import views
from .views import FiltrarAcabamentoView

urlpatterns = [
    path('novopedido', PedidoCreate.as_view(), name='novopedido'),
    path('filtrar_acabamento/', FiltrarAcabamentoView.as_view(), name='filtrar_acabamento'),
]