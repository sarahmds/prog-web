# tests/test_usabilidade.py
from django.test import TestCase
from django.urls import reverse

class UsabilidadeTest(TestCase):
    def test_mensagem_sem_dados(self):
        response = self.client.get(reverse("loja:lista"))
        self.assertContains(response, "Nenhum registro encontrado")
