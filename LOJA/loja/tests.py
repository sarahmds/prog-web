from django.test import TestCase
from django.urls import reverse
from .models import *
from .models import Produto

class ProdutoModelTest(TestCase):

    def test_criar_produto(self):
        produto = Produto.objects.create(
            Produto="Produto Teste",
            preco=10.00
        )

        self.assertEqual(produto.Produto, "Produto Teste")
        self.assertEqual(float(produto.preco), 10.00)



class ProdutoViewTest(TestCase):

    def setUp(self):
        Produto.objects.create(
            Produto="Produto Teste",
            preco=10.00,        
            promocao=False,
            destaque=False
        )

    def test_view_lista_produtos_status_code(self):
        response = self.client.get(reverse('produto'))
        self.assertEqual(response.status_code, 200)

    def test_view_lista_produtos_template(self):
        response = self.client.get(reverse('produto'))
        self.assertTemplateUsed(response, 'produto/produto.html')

    def test_view_lista_produtos_com_filtro(self):
        response = self.client.get(
            reverse('produto'),
            {'produto': 'Teste'}
        )
        self.assertEqual(response.status_code, 200)

