from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from loja.models import Produto, Fabricante, Categoria
from datetime import timedelta
from django.utils import timezone
from django.core.files.storage import FileSystemStorage

def create_produto_view(request, id=None):
    if request.method == 'POST':
        produto = request.POST.get("Produto")
        destaque = request.POST.get("destaque")
        promocao = request.POST.get("promocao")
        msgPromocao = request.POST.get("msgPromocao")
        preco = request.POST.get("preco")
        categoria = request.POST.get("CategoriaFk")
        fabricante = request.POST.get("FabricanteFk")

        try:
            obj_produto = Produto()
            obj_produto.Produto = produto
            obj_produto.destaque = bool(destaque)
            obj_produto.promocao = bool(promocao)
            obj_produto.msgPromocao = msgPromocao if msgPromocao else ""
            obj_produto.preco = float(preco) if preco else 0
            obj_produto.categoria = Categoria.objects.filter(id=categoria).first() if categoria != "-1" else None
            obj_produto.fabricante = Fabricante.objects.filter(id=fabricante).first() if fabricante != "-1" else None
            obj_produto.criado_em = timezone.now()
            obj_produto.alterado_em = obj_produto.criado_em

            if request.FILES.get('image'):
                imagefile = request.FILES['image']
                fs = FileSystemStorage()
                filename = fs.save(imagefile.name, imagefile)
                obj_produto.image = filename

            obj_produto.save()
            print(f"Produto {produto} salvo com sucesso")
        except Exception as e:
            print(f"Erro inserindo produto: {e}")
        return redirect("/produto")

    # Buscar categorias e fabricantes antes do dicionário
    categorias = Categoria.objects.all()
    fabricantes = Fabricante.objects.all()
    print("Categorias:", categorias)       # debug
    print("Fabricantes:", fabricantes)     # debug

    context = {
        'categorias': categorias,
        'fabricantes': fabricantes
    }
    return render(request, 'produto/produto-create.html', context=context)

@login_required
def edit_produto_view(request, id=None):
    produto = Produto.objects.filter(id=id).first() if id else None
    categorias = Categoria.objects.all()
    fabricantes = Fabricante.objects.all()
    context = {'produto': produto, 'categorias': categorias, 'fabricantes': fabricantes}
    return render(request, 'produto/produto-edit.html', context=context, status=200)

def edit_produto_postback(request, id=None):
    if request.method == 'POST':
        id = request.POST.get("id")
        produto_nome = request.POST.get("Produto")
        destaque = request.POST.get("destaque")
        promocao = request.POST.get("promocao")
        msgPromocao = request.POST.get("msgPromocao")
        categoria = request.POST.get("CategoriaFk")
        fabricante = request.POST.get("FabricanteFk")

        try:
            obj_produto = Produto.objects.filter(id=id).first()
            obj_produto.Produto = produto_nome
            obj_produto.destaque = bool(destaque)
            obj_produto.promocao = bool(promocao)
            obj_produto.msgPromocao = msgPromocao if msgPromocao else ""
            obj_produto.categoria = Categoria.objects.filter(id=categoria).first() if categoria != "-1" else None
            obj_produto.fabricante = Fabricante.objects.filter(id=fabricante).first() if fabricante != "-1" else None
            obj_produto.alterado_em = timezone.now()
            obj_produto.save()
            print(f"Produto {produto_nome} salvo com sucesso")
        except Exception as e:
            print(f"Erro salvando edição de produto: {e}")

    return redirect("/produto")

def list_produto_view(request):
    produto = request.GET.get("produto")
    destaque = request.GET.get("destaque")
    promocao = request.GET.get("promocao")
    categoria = request.GET.get("categoria")
    fabricante = request.GET.get("fabricante")
    dias = request.GET.get("dias")

    produtos = Produto.objects.all()
    if produto:
        produtos = produtos.filter(Produto__icontains=produto)
    if promocao:
        produtos = produtos.filter(promocao=promocao)
    if destaque:
        produtos = produtos.filter(destaque=destaque)
    if categoria:
        produtos = produtos.filter(categoria__Categoria=categoria)
    if fabricante:
        produtos = produtos.filter(fabricante__Fabricante=fabricante)
    if dias:
        now = timezone.now() - timedelta(days=int(dias))
        produtos = produtos.filter(criado_em__gte=now)

    return render(request, 'produto/produto.html', context={'produtos': produtos}, status=200)

def details_produto_view(request, id=None):
    produto = Produto.objects.filter(id=id).first() if id else None
    return render(request, 'produto/produto-details.html', context={'produto': produto}, status=200)

def delete_produto_view(request, id=None):
    produto = Produto.objects.filter(id=id).first() if id else None
    return render(request, 'produto/produto-delete.html', context={'produto': produto}, status=200)

def delete_produto_postback(request, id=None):
    if request.method == 'POST':
        id = request.POST.get("id")
        produto_nome = request.POST.get("Produto")
        try:
            Produto.objects.filter(id=id).delete()
            print(f"Produto {produto_nome} excluido com sucesso")
        except Exception as e:
            print(f"Erro excluindo produto: {e}")
    return redirect("/produto")
