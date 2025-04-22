from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .Fabricante import Fabricante
# loja/models/Categoria:
from loja.models import *
class Categoria(models.Model):
Categoria = models.CharField(null=False, max_length=100)
criado_em = models.DateTimeField(auto_now_add=True)
alterado_em = models.DateTimeField(auto_now=True)
def __str__(self):
return '{}'.format(self.Categoria)