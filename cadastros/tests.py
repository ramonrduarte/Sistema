# cadastros/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import Perfil, PerfilPuxador, Divisor, Puxador, Acabamento, ModeloPerfil


from django.test import TestCase
from .models import Perfil, Acabamento, ModeloPerfil

class PerfilUpdateTestCase(TestCase):
    def setUp(self):
        # Cria um acabamento para ser utilizado no perfil
        self.acabamento = Acabamento.objects.create(acabamento='Acabamento Teste', codigo_rgb='123456')
        # Cria um modelo perfil para ser utilizado no perfil
        self.modelo_perfil = ModeloPerfil.objects.create(modelo='Modelo Teste')

        # Cria uma instância de Perfil com os campos necessários preenchidos
        self.perfil = Perfil.objects.create(
            acabamento=self.acabamento,
            modelo=self.modelo_perfil,
            encaixe='1',
            encaixedivisor='2',
            encaixepuxador='1',
            preco=0.0,
            descricao='Descrição do perfil',
            codigo='123456',
            tipo_id=1,
            aba_perfil=0.0,
            aba_puxador=0.0,
            desconto_vidro=0.0,
            largura_perfil=0.0,
            largura_puxador=0.0
        )

    def test_context_data(self):
        # Verifica se as informações estão no contexto
        self.assertIn('perfilpuxador_ids', response.context)
        self.assertIn('divisor_ids', response.context)
        self.assertIn('puxador_ids', response.context)
        self.assertIn('perfilpuxador', response.context)
        self.assertIn('divisor', response.context)
        self.assertIn('puxador', response.context)
        self.assertIn('acabamentos', response.context)

        # Adicione mais verificações conforme necessário para garantir que os dados estejam corretos
