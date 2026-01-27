# tests/test_integracao.py
from django.test import TestCase
from loja.models import Produto

class IntegracaoTest(TestCase):
    def test_criar_e_listar_produto(self):
        Produto.objects.create(Produto="TI", preco=10)
        produtos = produto.objects.all()
        self.assertEqual(produtos.count(), 1)
