from django.test import TestCase
from loja.models import Produto
from django.db import IntegrityError

class IntegridadeTest(TestCase):
    def test_produto_descricao_obrigatoria(self):
        with self.assertRaises(IntegrityError):
            Produto.objects.create(descricao="")
