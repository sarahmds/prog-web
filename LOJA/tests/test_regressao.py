from django.test import TestCase
from loja.models import Produto

class RegressaoTest(TestCase):
    def test_nome_nao_duplica(self):
        Produto.objects.create(Produto="RH", preco=10)
        Produto.objects.create(Produto="RH", preco=10)
        self.assertEqual(Produto.objects.count(), 2)
