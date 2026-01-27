# tests/test_performance.py
import time
from django.test import TestCase
from django.urls import reverse

class PerformanceTest(TestCase):
    def test_tempo_resposta(self):
        inicio = time.time()
        self.client.get(reverse("loja:lista"))
        fim = time.time()
        self.assertLess(fim - inicio, 1)  # menos de 1 segundo
