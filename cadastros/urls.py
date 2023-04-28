from django.urls import path
from .views import AcabamentoCreate, ModeloPerfilCreate,ModeloPerfilPuxadorCreate, ModeloPuxadorCreate, ModeloDivisorCreate, ModeloDivisoriaAmbienteCreate, ModeloVidroCreate, TipoCreate, PerfilCreate, PerfilPuxadorCreate
from .views import AcabamentoUpdate, ModeloPerfilUpdate,ModeloPerfilPuxadorUpdate, ModeloPuxadorUpdate, ModeloDivisorUpdate, ModeloDivisoriaAmbienteUpdate, ModeloVidroUpdate, TipoUpdate, PerfilUpdate, PerfilPuxadorUpdate
from .views import AcabamentoDelete, ModeloPerfilDelete,ModeloPerfilPuxadorDelete, ModeloPuxadorDelete, ModeloDivisorDelete, ModeloDivisoriaAmbienteDelete, ModeloVidroDelete, TipoDelete, PerfilDelete, PerfilPuxadorDelete
from .views import AcabamentoList, TipoList, PerfilList, PerfilPuxadorList
from .views import Modelos

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

    path('editar/acabamento/<int:pk>/', AcabamentoUpdate.as_view(), name='editar-acabamento'),
    path('editar/modelo-perfil/<int:pk>/', ModeloPerfilUpdate.as_view(), name='editar-modelo-perfil'),
    path('editar/modelo-perfilpuxador/<int:pk>/', ModeloPerfilPuxadorUpdate.as_view(), name='editar-modelo-perfilpuxador'),
    path('editar/modelo-puxador/<int:pk>/', ModeloPuxadorUpdate.as_view(), name='editar-modelo-puxador'),
    path('editar/modelo-divisor/<int:pk>/', ModeloDivisorUpdate.as_view(), name='editar-modelo-divisor'),
    path('editar/modelo-divisoriaambiente/<int:pk>/', ModeloDivisoriaAmbienteUpdate.as_view(),name='editar-modelo-divisoriaambiente'),
    path('editar/modelo-vidro/<int:pk>/', ModeloVidroUpdate.as_view(), name='editar-modelo-vidro'),
    path('editar/tipo/<int:pk>/', TipoUpdate.as_view(), name='editar-tipo'),
    path('editar/perfil/<int:pk>/', PerfilUpdate.as_view(), name='editar-perfil'),
    path('editar/perfilpuxador/<int:pk>/', PerfilPuxadorUpdate.as_view(), name='editar-perfilpuxador'),

    path('excluir/acabamento/<int:pk>/', AcabamentoDelete.as_view(), name='excluir-acabamento'),
    path('excluir/modelo-perfil/<int:pk>/', ModeloPerfilDelete.as_view(), name='excluir-modelo-perfil'),
    path('excluir/modelo-perfilpuxador/<int:pk>/', ModeloPerfilPuxadorDelete.as_view(), name='excluir-modelo-perfilpuxador'),
    path('excluir/modelo-puxador/<int:pk>/', ModeloPuxadorDelete.as_view(), name='excluir-modelo-puxador'),
    path('excluir/modelo-divisor/<int:pk>/', ModeloDivisorDelete.as_view(), name='excluir-modelo-divisor'),
    path('excluir/modelo-divisoriaambiente/<int:pk>/', ModeloDivisoriaAmbienteDelete.as_view(),name='excluir-modelo-divisoriaambiente'),
    path('excluir/modelo-vidro/<int:pk>/', ModeloVidroDelete.as_view(), name='excluir-modelo-vidro'),
    path('excluir/tipo/<int:pk>/', TipoDelete.as_view(), name='excluir-tipo'),
    path('excluir/perfil/<int:pk>/', PerfilDelete.as_view(), name='excluir-perfil'),
    path('excluir/perfilpuxador/<int:pk>/', PerfilPuxadorDelete.as_view(), name='excluir-perfilpuxador'),

    path('listar/acabamento/', AcabamentoList.as_view(), name='listar-acabamento'),
    # path('listar/modelo-perfil/', ModeloPerfilList.as_view(), name='listar-modelo-perfil'),
    # path('listar/modelo-perfilpuxador/', ModeloPerfilPuxadorList.as_view(), name='listar-modelo-perfilpuxador'),
    path('listar/tipo/', TipoList.as_view(), name='listar-tipo'),
    path('listar/perfil/', PerfilList.as_view(), name='listar-perfil'),
    path('listar/perfilpuxador/', PerfilPuxadorList.as_view(), name='listar-perfilpuxador'),

    path('listar/modelos/', Modelos, name='listar-modelos'),


]