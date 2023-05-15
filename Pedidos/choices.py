from django.db.models import TextChoices

class StatusPedido(TextChoices):
    ABERTO = "A", "Aberto"
    CANCELADO = "C", "Cancelado"
    FINALIZADO = "F", "Finalizado"
    PRODUCAO = "P", "Produção"


class Abertura(TextChoices):
    DIREITA = "D", "Direita"
    ESQUERDA = "E", "Esquerda"
    CIMA = "C", "Cima"
    BAIXO = "B", "Baixo"