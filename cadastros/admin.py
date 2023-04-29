from django.contrib import admin
from .models import Acabamento, ModeloPerfil, ModeloPerfilPuxador, ModeloPuxador,ModeloDivisor, ModeloDivisoriaAmbiente, ModeloVidro, Tipo, Perfil, PerfilPuxador, Puxador

@admin.register(Acabamento)
class AcabamentoAdmin(admin.ModelAdmin):
    list_display = ('acabamento',)

@admin.register(ModeloPerfil)
class ModeloPerfilAdmin(admin.ModelAdmin):
    list_display = ('modelo',)

@admin.register(ModeloPerfilPuxador)
class ModeloPerfilPuxadorAdmin(admin.ModelAdmin):
    list_display = ('modelo',)

@admin.register(ModeloPuxador)
class ModeloPuxadorAdmin(admin.ModelAdmin):
    list_display = ('modelo',)

@admin.register(ModeloDivisor)
class ModeloDivisorAdmin(admin.ModelAdmin):
    list_display = ('modelo',)

@admin.register(ModeloDivisoriaAmbiente)
class ModeloDivisoriaAmbienteAdmin(admin.ModelAdmin):
    list_display = ('modelo',)

@admin.register(ModeloVidro)
class ModeloVidroAdmin(admin.ModelAdmin):
    list_display = ('modelo',)

@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ('tipo',)

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('codigo','descricao','preco','acabamento','tipo','modelo','encaixe','puxadorsobreposto','testando')

@admin.register(PerfilPuxador)
class PerfilPuxadorAdmin(admin.ModelAdmin):
    list_display = ('codigo','descricao','preco','acabamento','tipo','modelo','perfilencaixe')

@admin.register(Puxador)
class PuxadorAdmin(admin.ModelAdmin):
    list_display = ('codigo','descricao','preco','acabamento','tipo','modelo')