from django.urls import path
from .views import AcabamentoCreate, ModeloPerfilCreate, ModeloPerfilPuxadorCreate, ModeloPuxadorCreate, ModeloDivisorCreate, ModeloDivisoriaAmbienteCreate, ModeloVidroCreate, TipoCreate, PerfilCreate, PerfilPuxadorCreate, PuxadorCreate, DivisorCreate, DivisoriaAmbienteCreate, VidroCreate
from .views import AcabamentoUpdate, ModeloPerfilUpdate, ModeloPerfilPuxadorUpdate, ModeloPuxadorUpdate, ModeloDivisorUpdate, ModeloDivisoriaAmbienteUpdate, ModeloVidroUpdate, TipoUpdate, PerfilUpdate, PerfilPuxadorUpdate, PuxadorUpdate, DivisorUpdate, DivisoriaAmbienteUpdate, VidroUpdate
from .views import AcabamentoDelete, ModeloPerfilDelete, ModeloPerfilPuxadorDelete, ModeloPuxadorDelete, ModeloDivisorDelete, ModeloDivisoriaAmbienteDelete, ModeloVidroDelete, TipoDelete, PerfilDelete, PerfilPuxadorDelete, PuxadorDelete, DivisorDelete, DivisoriaAmbienteDelete, VidroDelete
from .views import AcabamentoList, TipoList, PerfilList, PerfilPuxadorList, PuxadorList, DivisorList, DivisoriaAmbienteList, VidroList
from .views import Modelos
from . import views

urlpatterns = [
    path('cadastrar/acabamento', AcabamentoCreate.as_view(), name='cadastrar-acabamento'),
    path('cadastrar/modelo-perfil', ModeloPerfilCreate.as_view(), name='cadastrar-modelo-perfil'),
    path('cadastrar/modelo-perfilpuxador', ModeloPerfilPuxadorCreate.as_view(), name='cadastrar-modelo-perfilpuxador'),
    path('cadastrar/modelo-puxador', ModeloPuxadorCreate.as_view(), name='cadastrar-modelo-puxador'),
    path('cadastrar/modelo-divisor', ModeloDivisorCreate.as_view(), name='cadastrar-modelo-divisor'),
    path('cadastrar/modelo-divisoriaambiente', ModeloDivisoriaAmbienteCreate.as_view(), name='cadastrar-modelo-divisoriaambiente'),
    path('cadastrar/modelo-vidro', ModeloVidroCreate.as_view(), name='cadastrar-modelo-vidro'),
    path('cadastrar/tipo', TipoCreate.as_view(), name='cadastrar-tipo'),
    path('cadastrar/perfil', PerfilCreate.as_view(), name='cadastrar-perfil'),
    path('cadastrar/perfilpuxador', PerfilPuxadorCreate.as_view(), name='cadastrar-perfilpuxador'),
    path('cadastrar/puxador', PuxadorCreate.as_view(), name='cadastrar-puxador'),
    path('cadastrar/divisor', DivisorCreate.as_view(), name='cadastrar-divisor'),
    path('cadastrar/divisoriaambiente', DivisoriaAmbienteCreate.as_view(), name='cadastrar-divisoriaambiente'),
    path('cadastrar/vidro', VidroCreate.as_view(), name='cadastrar-vidro'),

    path('editar/acabamento/<int:pk>/', AcabamentoUpdate.as_view(), name='editar-acabamento'),
    path('editar/modelo-perfil/<int:pk>/', ModeloPerfilUpdate.as_view(), name='editar-modelo-perfil'),
    path('editar/modelo-perfilpuxador/<int:pk>/', ModeloPerfilPuxadorUpdate.as_view(), name='editar-modelo-perfilpuxador'),
    path('editar/modelo-puxador/<int:pk>/', ModeloPuxadorUpdate.as_view(), name='editar-modelo-puxador'),
    path('editar/modelo-divisor/<int:pk>/', ModeloDivisorUpdate.as_view(), name='editar-modelo-divisor'),
    path('editar/modelo-divisoriaambiente/<int:pk>/', ModeloDivisoriaAmbienteUpdate.as_view(), name='editar-modelo-divisoriaambiente'),
    path('editar/modelo-vidro/<int:pk>/', ModeloVidroUpdate.as_view(), name='editar-modelo-vidro'),
    path('editar/tipo/<int:pk>/', TipoUpdate.as_view(), name='editar-tipo'),
    path('editar/perfil/<int:pk>/', PerfilUpdate.as_view(), name='editar-perfil'),
    path('editar/perfilpuxador/<int:pk>/', PerfilPuxadorUpdate.as_view(), name='editar-perfilpuxador'),
    path('editar/puxador/<int:pk>/', PuxadorUpdate.as_view(), name='editar-puxador'),
    path('editar/divisor/<int:pk>/', DivisorUpdate.as_view(), name='editar-divisor'),
    path('editar/divisoriaambiente/<int:pk>/', DivisoriaAmbienteUpdate.as_view(), name='editar-divisoriaambiente'),
    path('editar/vidro/<int:pk>/', VidroUpdate.as_view(), name='editar-vidro'),

    path('excluir/acabamento/<int:pk>/', AcabamentoDelete.as_view(), name='excluir-acabamento'),
    path('excluir/modelo-perfil/<int:pk>/', ModeloPerfilDelete.as_view(), name='excluir-modelo-perfil'),
    path('excluir/modelo-perfilpuxador/<int:pk>/', ModeloPerfilPuxadorDelete.as_view(), name='excluir-modelo-perfilpuxador'),
    path('excluir/modelo-puxador/<int:pk>/', ModeloPuxadorDelete.as_view(), name='excluir-modelo-puxador'),
    path('excluir/modelo-divisor/<int:pk>/', ModeloDivisorDelete.as_view(), name='excluir-modelo-divisor'),
    path('excluir/modelo-divisoriaambiente/<int:pk>/', ModeloDivisoriaAmbienteDelete.as_view(), name='excluir-modelo-divisoriaambiente'),
    path('excluir/modelo-vidro/<int:pk>/', ModeloVidroDelete.as_view(), name='excluir-modelo-vidro'),
    path('excluir/tipo/<int:pk>/', TipoDelete.as_view(), name='excluir-tipo'),
    path('excluir/perfil/<int:pk>/', PerfilDelete.as_view(), name='excluir-perfil'),
    path('excluir/perfilpuxador/<int:pk>/', PerfilPuxadorDelete.as_view(), name='excluir-perfilpuxador'),
    path('excluir/puxador/<int:pk>/', PuxadorDelete.as_view(), name='excluir-puxador'),
    path('excluir/divisor/<int:pk>/', DivisorDelete.as_view(), name='excluir-divisor'),
    path('excluir/divisoriaambiente/<int:pk>/', DivisoriaAmbienteDelete.as_view(), name='excluir-divisoriaambiente'),
    path('excluir/vidro/<int:pk>/', VidroDelete.as_view(), name='excluir-vidro'),

    path('listar/acabamento/', AcabamentoList.as_view(), name='listar-acabamento'),
    path('listar/tipo/', TipoList.as_view(), name='listar-tipo'),
    path('listar/perfil/', PerfilList.as_view(), name='listar-perfil'),
    path('listar/perfilpuxador/', PerfilPuxadorList.as_view(), name='listar-perfilpuxador'),
    path('listar/puxador/', PuxadorList.as_view(), name='listar-puxador'),
    path('listar/divisor/', DivisorList.as_view(), name='listar-divisor'),
    path('listar/divisoriaambiente/', DivisoriaAmbienteList.as_view(), name='listar-divisoriaambiente'),
    path('listar/vidro/', VidroList.as_view(), name='listar-vidro'),

    path('listar/modelos/', Modelos, name='listar-modelos'),
    path('filtrar-perfil/', views.filtrar_perfil, name='filtrar_perfil'),
    path('filtrar-divisor/', views.filtrar_divisor, name='filtrar_divisor'),
    path('filtrar-puxador/', views.filtrar_puxador, name='filtrar_puxador'),

]

htmx_urlpatterns = [


]

urlpatterns += htmx_urlpatterns