from django.urls import path
from .views import PedidoCreate
from . import views
from .views import BuscarPerfil, BuscarPerfilPuxador, BuscarDivisor, BuscarPuxador, BuscarVidro
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('Pedidos/', PedidoCreate.as_view(), name='Pedidos'),
    path('buscar_perfil/', BuscarPerfil.as_view(), name='buscar_perfil'),
    path('buscar_PerfilPuxador/', BuscarPerfilPuxador.as_view(), name='buscar_PerfilPuxador'),
    path('buscar_Divisor/', BuscarDivisor.as_view(), name='buscar_Divisor'),
    path('buscar_Puxador/', BuscarPuxador.as_view(), name='buscar_Puxador'),
    path('buscar_Vidro/', BuscarVidro.as_view(), name='buscar_Vidro'),
    path('obter_acabamentos/', views.obter_acabamentos, name='obter_acabamentos'),
    path('obter_codigo_rgb/', views.obter_codigo_rgb, name='obter_codigo_rgb'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
