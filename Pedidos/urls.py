from django.urls import path
from . import views
from .views import PedidoCreate

urlpatterns = [
    # path('novopedido', views.home, name='home'),
    path('novopedido', PedidoCreate.as_view(), name='novopedido'),
]