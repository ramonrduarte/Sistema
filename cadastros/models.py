from django.db import models
"from multiselectfield import MultiSelectField"
"from django.core.validators import MaxValueValidator"
"from Pedidos.choices import Linha"

TESTEMODELO = (('nao possui', 'Não possui'),
              ('Vinte',     '2020'),
              ('trinta',    '3030'),
              ('Quarenta',  '4040'),
              ('Cinquenta', '5050'),
              ('Sessenta',  '6060'),
              ('Setenta',   '7070'))

ENCAIXE = (('1', 'Sim'),
    ('2', 'Não'))

LINHA = (('Doppio', 'Doppio'),
        ('Mil', 'Mil'))

POSICAODIVISORIA = (('Travessa/Inferior', 'Travessa/Inferior'),
                    ('Superior', 'Superior'),
                    ('Lateral', 'Lateral'),
                    ('Superior/Inferior', 'Superior/Inferior'),
                    ('Inferior', 'Inferior'),
                    ('Travessa', 'Travessa'))

TIPODIVISOR = (('Aparente', 'Aparente'),
                    ('Oculto', 'Oculto'))


class Acabamento(models.Model):
    acabamento = models.CharField(max_length=50, unique=True)
    codigo_rgb = models.CharField(max_length=15, verbose_name="Código RGB",)

    class Meta:
        verbose_name = 'Acabamento'
        verbose_name_plural = 'Acabamentos'
        ordering = ["acabamento"]

    def __str__(self):
        return self.acabamento


class BaseModelo(models.Model):
    modelo = models.CharField(max_length=10, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.modelo


class ModeloPerfil(BaseModelo):
    class Meta:
        verbose_name = 'Modelo Perfil'
        verbose_name_plural = 'Modelo Perfis'
        ordering = ["modelo"]


class ModeloPerfilPuxador(BaseModelo):
    class Meta:
        verbose_name = 'Modelo Perfil Puxador'
        verbose_name_plural = 'Modelo Perfis Puxadores'
        ordering = ["modelo"]


class ModeloPuxador(BaseModelo):
    class Meta:
        verbose_name = 'Modelo Puxador'
        verbose_name_plural = 'Modelo Puxadores'
        ordering = ["modelo"]


class ModeloDivisor(BaseModelo):
    class Meta:
        verbose_name = 'Modelo Divisor'
        verbose_name_plural = 'Modelo Divisores'
        ordering = ["modelo"]


class ModeloDivisoriaAmbiente(BaseModelo):
    class Meta:
        verbose_name = 'Modelo Divisoria Ambiente'
        verbose_name_plural = 'Modelos Divisorias Ambiente'
        ordering = ["modelo"]


class ModeloVidro(BaseModelo):
    class Meta:
        verbose_name = 'Modelo Vidro'
        verbose_name_plural = 'Modelos Vidros'
        ordering = ["modelo"]


class Tipo(models.Model):
    tipo = models.CharField(max_length=30, unique=True)

    class Meta:
        ordering = ["tipo"]

    def __str__(self):
        return self.tipo


class ItemBase(models.Model):
    codigo = models.CharField(max_length=6, verbose_name="Código", unique=True)
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    preco = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Preço")
    acabamento = models.ForeignKey('Acabamento', on_delete=models.PROTECT)
    tipo = models.ForeignKey('Tipo', on_delete=models.PROTECT)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.descricao


class PerfilPuxador(ItemBase):
    modelo = models.ForeignKey(ModeloPerfilPuxador, on_delete=models.PROTECT)
    largura_perfil = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Largura Perfil")
    aba_perfil = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Aba Perfil")
    desconto_vidro = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Desconto P/Vidro")
    largura_puxador = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Largura Puxador")
    aba_puxador = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Aba Puxador")

    class Meta:
        verbose_name = 'Perfil Puxador'
        verbose_name_plural = 'Perfis Puxadores'
        ordering = ["descricao"]


class Puxador(ItemBase):
    modelo = models.ForeignKey(ModeloPuxador, on_delete=models.PROTECT)
    desconto_puxador = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Desconto Puxador")

    class Meta:
        verbose_name = 'Puxador'
        verbose_name_plural = 'Puxadores'
        ordering = ["descricao"]


class Divisor(ItemBase):
    modelo = models.ForeignKey(ModeloDivisor, on_delete=models.PROTECT)
    tipodivisor = models.CharField(choices=TIPODIVISOR, max_length=50, verbose_name="Tipo Divisor")
    espdivisor = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Espessura Divisor")

    class Meta:
        verbose_name = 'Perfil Divisor'
        verbose_name_plural = 'Perfis Divisores'
        ordering = ["descricao"]


class DivisoriaAmbiente(ItemBase):
    modelo = models.ForeignKey(ModeloDivisoriaAmbiente, on_delete=models.PROTECT)
    linha = models.CharField(choices=LINHA, max_length=50)
    posicao = models.CharField(choices=POSICAODIVISORIA, max_length=50)

    class Meta:
        verbose_name = 'Perfil Divisoria Ambiente'
        verbose_name_plural = 'Perfis Divisorias Ambiente'
        ordering = ["descricao"]


class Vidro(models.Model):
    codigo = models.CharField(max_length=6, verbose_name="Código", unique=True)
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    preco = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Preço")
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    modelo = models.ForeignKey(ModeloVidro, on_delete=models.PROTECT)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Vidro'
        verbose_name_plural = 'Vidros'
        ordering = ["descricao"]

    def __str__(self):
        return self.descricao


class Perfil(ItemBase):
    modelo = models.ForeignKey(ModeloPerfil, on_delete=models.PROTECT)
    encaixe = models.CharField(max_length=3, choices=ENCAIXE, blank=True, null=True)
    perfilpuxador = models.ManyToManyField(PerfilPuxador, verbose_name="Perfil Puxador", blank=True)
    encaixedivisor = models.CharField(max_length=3, choices=ENCAIXE, blank=True, null=True)
    divisor = models.ManyToManyField(Divisor, verbose_name="Divisor", blank=True)
    encaixepuxador = models.CharField(max_length=3, choices=ENCAIXE, blank=True, null=True)
    puxador = models.ManyToManyField(Puxador, verbose_name="Puxador", blank=True)
    largura_perfil = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Largura Perfil")
    aba_perfil = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Aba Perfil")
    desconto_vidro = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Desconto P/Vidro")
    largura_puxador = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Largura Puxador")
    aba_puxador = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Aba Puxador")

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
        ordering = ["descricao"]


class PuxadorIntermediario(models.Model):
    perfil = models.ForeignKey(Perfil, related_name="puxadores_perfil", on_delete=models.PROTECT, blank=True, null=True)
    puxador = models.ForeignKey(Puxador, related_name="puxadores_perfil", on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return "{} - {} " .format(self.puxador.descricao, self.perfil.descricao)