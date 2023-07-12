from django.urls import path
from .views import PedidoCreate
from . import views
from .views import FiltrarAcabamentoView, buscar_PerfilPuxador, buscar_Divisor, buscar_Puxador, filtrar_divisoriaView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('orcamento/', PedidoCreate.as_view(), name='orcamento'),
    path('filtrar_acabamento/', FiltrarAcabamentoView.as_view(), name='filtrar_acabamento'),
    path('buscar_PerfilPuxador/', buscar_PerfilPuxador.as_view(), name='buscar_PerfilPuxador'),
    path('buscar_Divisor/', buscar_Divisor.as_view(), name='buscar_Divisor'),
    path('buscar_Puxador/', buscar_Puxador.as_view(), name='buscar_Puxador'),
    path('filtrar_divisoria/', filtrar_divisoriaView.as_view(), name='filtrar_divisoria'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)