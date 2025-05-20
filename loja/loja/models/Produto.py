# loja/models/Produto.py
from loja.models import *

class Produto(models.Model):
    nome = models.CharField(null=False, max_length=100)  # Renomeado de Produto para nome
    destaque = models.BooleanField(default=True)
    promocao = models.BooleanField(default=True)
    msgPromocao = models.CharField(null=True, max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    estoque = models.IntegerField(default=0)  # Adicionado o campo estoque
    categoria = models.ForeignKey(Categoria, null=True, related_name='categoria', on_delete=models.SET_NULL)
    fabricante = models.ForeignKey(Fabricante, null=True, related_name='fabricante', on_delete=models.SET_NULL)
    criado_em = models.DateTimeField(auto_now_add=True)
    search_fields = ('Produto',)
    alterado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome  # Retorna o nome do produto
