# tests/test_instalacao.py
from django.test import TestCase
from django.apps import apps

class InstalacaoConfigTest(TestCase):
    def test_app_registrado(self):
        self.assertTrue(apps.is_installed("loja"))
