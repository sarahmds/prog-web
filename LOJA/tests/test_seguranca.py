# tests/test_seguranca.py
from django.test import TestCase
from django.urls import reverse

class SegurancaTest(TestCase):
    def test_area_protegida_sem_login(self):
        response = self.client.get(reverse("loja:area_restrita"))
        self.assertEqual(response.status_code, 302)  # redireciona para login
