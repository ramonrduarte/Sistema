from django.db.models import TextChoices

class StatusPedido(TextChoices):
    ABERTO = "A", "Aberto"
    CANCELADO = "C", "Cancelado"
    FINALIZADO = "F", "Finalizado"
    PRODUCAO = "P", "Produção"