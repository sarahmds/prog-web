from django.test import TestCase
from loja.models import Produto

class VolumeTest(TestCase):
    def test_muitos_registros(self):
        for i in range(50):
            Produto.objects.create(Produto=f"Produto {i}", preco=10)
        self.assertEqual(Produto.objects.count(), 50)
