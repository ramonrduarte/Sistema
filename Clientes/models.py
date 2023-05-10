from django.db import models

class Cliente(models.Model):
    codigo = models.CharField(max_length=6, verbose_name="Código")
    nome = models.CharField(max_length=150, verbose_name="Nome")
    cpf_cnpj = models.CharField(max_length=20, verbose_name="CPF/CNPJ")
    cep = models.CharField(max_length=9, verbose_name="CEP")
    logradouro = models.CharField(max_length=150, verbose_name="Logradouro")
    numero = models.CharField(max_length=6, verbose_name="Número")
    bairro = models.CharField(max_length=150, verbose_name="Bairro")
    cidade = models.CharField(max_length=150, verbose_name="Cidade")
    telefone = models.CharField(max_length=15, verbose_name="Telefone")

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ["nome"]

    def __str__(self):
        return self.nome