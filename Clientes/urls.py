from django.urls import path
from .views import ClientesCreate, ClientesUpdate, ClientesDelete, ClientesList, buscar_cliente

urlpatterns = [
    path('cadastrar/clientes', ClientesCreate.as_view(), name='cadastrar-clientes'),
    path('editar/clientes/<int:pk>/', ClientesUpdate.as_view(), name='editar-clientes'),
    path('excluir/clientes/<int:pk>/', ClientesDelete.as_view(), name='excluir-clientes'),
    path('listar/clientes/', ClientesList.as_view(), name='listar-clientes'),
    path('buscar-cliente/', buscar_cliente, name='buscar-cliente'),
]
