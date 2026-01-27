# tests/test_funcional.py
from django.test import TestCase
from django.urls import reverse

class FuncionalTest(TestCase):
    def test_pagina_lista_carrega(self):
        response = self.client.get(reverse("loja:lista"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Lista de")
