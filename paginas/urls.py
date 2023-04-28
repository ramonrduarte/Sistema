from django.urls import path
from .views import PaginaInicial, PaginaLogin, PaginaOrcamento

urlpatterns = [
    path('', PaginaInicial.as_view(), name='inicio'),
    # path('login', PaginaLogin.as_view(), name='login'),
    path('orcamento', PaginaOrcamento.as_view(), name='orcamento'),


]