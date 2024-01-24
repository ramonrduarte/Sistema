from rest_framework import serializers
from .models import Perfil

#
# class ModeloPerfilSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     descricao = serializers.CharField(max_length=255)
#     preco = serializers.DecimalField(max_digits=10, decimal_places=2)
#     modelo = serializers.CharField(max_length=255)
#
#     def to_representation(self, instance):
#         # Certifique-se de que todos os campos são serializáveis para JSON
#         return {
#             'id': int(instance.id),
#             'codigo': str(instance.codigo),
#             'descricao': str(f"({instance.codigo}) {instance.descricao}"),
#             'preco': float(instance.preco),
#             'modelo': str(instance.modelo),
#         }

class PerfilSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    descricao = serializers.CharField(max_length=255)
    preco = serializers.DecimalField(max_digits=10, decimal_places=2)
    modelo = serializers.CharField(max_length=255)

    def to_representation(self, instance):
        return {
            'id': int(instance.id),
            'descricao': str(f"({instance.codigo}) {instance.descricao}"),
            'preco': float(instance.preco),
            'modelo': str(instance.modelo),
        }


class PerfilPuxadorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    descricao = serializers.CharField(max_length=255)
    preco = serializers.DecimalField(max_digits=10, decimal_places=2)
    modelo = serializers.CharField(max_length=255)

    def to_representation(self, instance):
        return {
            'id': int(instance.id),
            'descricao': str(f"({instance.codigo}) {instance.descricao}"),
            'preco': float(instance.preco),
            'modelo': str(instance.modelo),
        }

class PuxadorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    descricao = serializers.CharField(max_length=255)
    preco = serializers.DecimalField(max_digits=10, decimal_places=2)
    modelo = serializers.CharField(max_length=255)

    def to_representation(self, instance):
        return {
            'id': int(instance.id),
            'descricao': str(f"({instance.codigo}) {instance.descricao}"),
            'preco': float(instance.preco),
            'modelo': str(instance.modelo),
        }

class VidroSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    descricao = serializers.CharField(max_length=255)
    preco = serializers.DecimalField(max_digits=10, decimal_places=2)
    modelo = serializers.CharField(max_length=255)

    def to_representation(self, instance):
        return {
            'id': int(instance.id),
            'descricao': str(f"({instance.codigo}) {instance.descricao}"),
            'nome': str(instance.descricao),
            'preco': float(instance.preco),
            'modelo': str(instance.modelo),
        }

class DivisorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    descricao = serializers.CharField(max_length=255)
    preco = serializers.DecimalField(max_digits=10, decimal_places=2)
    modelo = serializers.CharField(max_length=255)

    def to_representation(self, instance):
        return {
            'id': int(instance.id),
            'descricao': str(f"({instance.codigo}) {instance.descricao}"),
            'preco': float(instance.preco),
            'modelo': str(instance.modelo),
        }