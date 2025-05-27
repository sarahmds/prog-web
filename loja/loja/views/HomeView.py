from django.shortcuts import render #type: ignore
from loja.models import Produto
produto = request.GET.get("produto") #type: ignore
produtos = Produto.objects.all()
if produto is not None:
    produtos = produtos.filter(Produto__contains=produto)
def home_view(request):
    return render(request, template_name='home/home.html', status=200)