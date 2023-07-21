from django.urls import path
from .views import PedidoCreate
from . import views
from .views import FiltrarAcabamentoView, buscar_PerfilPuxador, buscar_Divisor, buscar_Puxador, buscar_Vidro, filtrar_divisoriaView, carregar_divinferiorView, carregar_divlateralView, carregar_divdivisorView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('Pedidos/', PedidoCreate.as_view(), name='Pedidos'),
    path('filtrar_acabamento/', FiltrarAcabamentoView.as_view(), name='filtrar_acabamento'),
    path('buscar_PerfilPuxador/', buscar_PerfilPuxador.as_view(), name='buscar_PerfilPuxador'),
    path('buscar_Divisor/', buscar_Divisor.as_view(), name='buscar_Divisor'),
    path('buscar_Puxador/', buscar_Puxador.as_view(), name='buscar_Puxador'),
    path('buscar_Vidro/', buscar_Vidro.as_view(), name='buscar_Vidro'),
    path('filtrar_divisoria/', filtrar_divisoriaView.as_view(), name='filtrar_divisoria'),
    path('carregar_divinferior/', carregar_divinferiorView.as_view(), name='carregar_divinferior'),
    path('carregar_divlateral/', carregar_divlateralView.as_view(), name='carregar_divlateral'),
    path('carregar_divdivisor/', carregar_divdivisorView.as_view(), name='carregar_divdivisor'),
    path('obter_acabamentos_divisoria_ambiente/', views.obter_acabamentos_divisoria_ambiente, name='obter_acabamentos_divisoria_ambiente'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)