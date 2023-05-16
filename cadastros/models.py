from django.db import models
from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator



# Create your models here.

TESTEMODELO = (('nao possui', 'Não possui'),
              ('Vinte', '2020'),
              ('trinta', '3030'),
              ('Quarenta', '4040'),
              ('Cinquenta', '5050'),
              ('Sessenta', '6060'),
              ('Setenta', '7070'))

ENCAIXE = (('1','Sim'),
    ('2','Não'))

LINHA = (('Doppio','Doppio'),
        ('mil','1000'))

POSICAODIVISORIA = (('Travessa/Inferior','Travessa/Inferior'),
                    ('Superior','Superior'),
                    ('Lateral','Lateral'),
                    ('Superior/Inferior','Superior/Inferior'),
                    ('Inferior','Inferior'),
                    ('Travessa','Travessa'))

class Acabamento(models.Model):
    acabamento = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Acabamento'
        verbose_name_plural = 'Acabamentos'
        ordering = ["acabamento"]

    def __str__(self):
        return self.acabamento


class ModeloPerfil(models.Model):
    modelo = models.CharField(max_length=10, unique=True)


    class Meta:
        verbose_name = 'Modelo Perfil'
        verbose_name_plural = 'Modelo Perfis'
        ordering = ["modelo"]

    def __str__(self):
        return self.modelo

class ModeloPerfilPuxador(models.Model):
    modelo = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = 'Modelo Perfil Puxador'
        verbose_name_plural = 'Modelo Perfis Puxadores'
        ordering = ["modelo"]

    def __str__(self):
        return self.modelo

class ModeloPuxador(models.Model):
    modelo = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = 'Modelo Puxador'
        verbose_name_plural = 'Modelo Puxadores'
        ordering = ["modelo"]

    def __str__(self):
        return self.modelo


class ModeloDivisor(models.Model):
    modelo = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = 'Modelo Divisor'
        verbose_name_plural = 'Modelo Divisores'
        ordering = ["modelo"]

    def __str__(self):
        return self.modelo


class ModeloDivisoriaAmbiente(models.Model):
    modelo = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = 'Modelo Divisoria Ambiente'
        verbose_name_plural = 'Modelos Divisorias Ambiente'
        ordering = ["modelo"]

    def __str__(self):
        return self.modelo


class ModeloVidro(models.Model):
    modelo = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = 'Modelo Vidro'
        verbose_name_plural = 'Modelos Vidros'
        ordering = ["modelo"]

    def __str__(self):
        return self.modelo

class Tipo(models.Model):
    tipo = models.CharField(max_length=30, unique=True)

    class Meta:
        ordering = ["tipo"]

    def __str__(self):
        return self.tipo


class PerfilPuxador(models.Model):
    codigo = models.CharField(max_length=6, verbose_name="Código")
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    preco = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Preço")
    acabamento = models.ForeignKey(Acabamento, on_delete=models.PROTECT)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    modelo = models.ForeignKey(ModeloPerfilPuxador, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Perfil Puxador'
        verbose_name_plural = 'Perfis Puxadores'
        ordering = ["descricao"]

    def __str__(self):
        return self.descricao


class Puxador(models.Model):
    codigo = models.CharField(max_length=6, verbose_name="Código")
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    preco = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Preço")
    acabamento = models.ForeignKey(Acabamento, on_delete=models.PROTECT)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    modelo = models.ForeignKey(ModeloPuxador, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Puxador'
        verbose_name_plural = 'Puxadores'
        ordering = ["descricao"]

    def __str__(self):
        return self.descricao

class Divisor(models.Model):
    codigo = models.CharField(max_length=6, verbose_name="Código")
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    preco = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Preço")
    acabamento = models.ForeignKey(Acabamento, on_delete=models.PROTECT)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    modelo = models.ForeignKey(ModeloDivisor, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Perfil Divisor'
        verbose_name_plural = 'Perfis Divisores'
        ordering = ["descricao"]

    def __str__(self):
        return self.descricao

class DivisoriaAmbiente(models.Model):
    codigo = models.CharField(max_length=6, verbose_name="Código")
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    preco = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Preço")
    acabamento = models.ForeignKey(Acabamento, on_delete=models.PROTECT)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    modelo = models.ForeignKey(ModeloDivisoriaAmbiente, on_delete=models.PROTECT)
    linha = models.CharField(choices=LINHA, max_length=50)
    posicao = models.CharField(choices=POSICAODIVISORIA, max_length=50)

    class Meta:
        verbose_name = 'Perfil Divisoria Ambiente'
        verbose_name_plural = 'Perfis Divisorias Ambiente'
        ordering = ["descricao"]

    def __str__(self):
        return self.descricao

class Vidro(models.Model):
    codigo = models.CharField(max_length=6, verbose_name="Código")
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    preco = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Preço")
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    modelo = models.ForeignKey(ModeloVidro, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Vidro'
        verbose_name_plural = 'Vidros'
        ordering = ["descricao"]

    def __str__(self):
        return self.descricao


class Perfil(models.Model):
    codigo = models.CharField(max_length=6, verbose_name="Código", unique=True)
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    preco = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Preço")
    acabamento = models.ForeignKey(Acabamento, on_delete=models.PROTECT)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    modelo = models.ForeignKey(ModeloPerfil, on_delete=models.PROTECT)
    encaixe = models.CharField(max_length=3, choices=ENCAIXE, blank=True, null=True)
    perfil_puxador = models.ForeignKey(PerfilPuxador, on_delete=models.PROTECT, verbose_name="Perfil Puxador",blank=True, null=True)
    encaixepuxador = models.CharField(max_length=3, choices=ENCAIXE, blank=True, null=True)
    puxadorsobreposto = models.ManyToManyField(Puxador, related_name="puxadores", through="PuxadorIntermediario")

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
        ordering = ["descricao"]

    def __str__(self):
        return self.descricao


class PuxadorIntermediario(models.Model):
    perfil = models.ForeignKey(Perfil, related_name="puxadores_perfil", on_delete=models.PROTECT, blank=True, null=True)
    puxador = models.ForeignKey(Puxador, related_name="puxadores_perfil", on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return "{} - {} " .format(self.puxador.descricao, self.perfil.descricao)