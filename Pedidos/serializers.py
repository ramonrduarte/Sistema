from rest_framework import serializers


class PerfilSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    descricao = serializers.CharField(max_length=255)
    preco = serializers.DecimalField(max_digits=10, decimal_places=2)
    modelo = serializers.CharField(max_length=255)
    tipo = serializers.CharField(max_length=255)
    largura_perfil = serializers.DecimalField(max_digits=10, decimal_places=2)
    aba_perfil = serializers.DecimalField(max_digits=10, decimal_places=2)
    desconto_vidro = serializers.DecimalField(max_digits=10, decimal_places=2)
    largura_puxador = serializers.DecimalField(max_digits=10, decimal_places=2)
    aba_puxador = serializers.DecimalField(max_digits=10, decimal_places=2)

    def to_representation(self, instance):
        return {
            'id': int(instance.id),
            'codigo': int(instance.codigo),
            'nome': str(instance.descricao),
            'descricao': str(f"({instance.codigo}) {instance.descricao}"),
            'preco': float(instance.preco),
            'modelo': str(instance.modelo),
            'tipo': str(instance.tipo),
            'largura_perfil': float(instance.largura_perfil),
            'aba_perfil': float(instance.aba_perfil),
            'desconto_vidro': float(instance.desconto_vidro),
            'largura_puxador': float(instance.largura_puxador),
            'aba_puxador': float(instance.aba_puxador),
        }


class PerfilPuxadorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    descricao = serializers.CharField(max_length=255)
    preco = serializers.DecimalField(max_digits=10, decimal_places=2)
    modelo = serializers.CharField(max_length=255)
    largura_perfil = serializers.DecimalField(max_digits=10, decimal_places=2)
    aba_perfil = serializers.DecimalField(max_digits=10, decimal_places=2)
    desconto_vidro = serializers.DecimalField(max_digits=10, decimal_places=2)
    largura_puxador = serializers.DecimalField(max_digits=10, decimal_places=2)
    aba_puxador = serializers.DecimalField(max_digits=10, decimal_places=2)

    def to_representation(self, instance):
        return {
            'id': int(instance.id),
            'codigo': int(instance.codigo),
            'nome': str(instance.descricao),
            'descricao': str(f"({instance.codigo}) {instance.descricao}"),
            'preco': float(instance.preco),
            'modelo': str(instance.modelo),
            'largura_perfil': float(instance.largura_perfil),
            'aba_perfil': float(instance.aba_perfil),
            'desconto_vidro': float(instance.desconto_vidro),
            'largura_puxador': float(instance.largura_puxador),
            'aba_puxador': float(instance.aba_puxador),
        }

class PuxadorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    descricao = serializers.CharField(max_length=255)
    preco = serializers.DecimalField(max_digits=10, decimal_places=2)
    modelo = serializers.CharField(max_length=255)
    desconto_puxador = serializers.DecimalField(max_digits=10, decimal_places=2)

    def to_representation(self, instance):
        return {
            'id': int(instance.id),
            'codigo': int(instance.codigo),
            'nome': str(instance.descricao),
            'descricao': str(f"({instance.codigo}) {instance.descricao}"),
            'preco': float(instance.preco),
            'modelo': str(instance.modelo),
            'desconto_puxador': float(instance.desconto_puxador),
        }

class VidroSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    descricao = serializers.CharField(max_length=255)
    preco = serializers.DecimalField(max_digits=10, decimal_places=2)
    modelo = serializers.CharField(max_length=255)

    def to_representation(self, instance):
        return {
            'id': int(instance.id),
            'codigo': int(instance.codigo),
            'nome': str(instance.descricao),
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
    tipodivisor = serializers.CharField(max_length=255)
    espdivisor = serializers.DecimalField(max_digits=10, decimal_places=2)


    def to_representation(self, instance):
        return {
            'id': int(instance.id),
            'codigo': int(instance.codigo),
            'nome': str(instance.descricao),
            'descricao': str(f"({instance.codigo}) {instance.descricao}"),
            'preco': float(instance.preco),
            'modelo': str(instance.modelo),
            'tipodivisor': str(instance.tipodivisor),
            'espdivisor': float(instance.espdivisor),
        }