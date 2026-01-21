from django.shortcuts import render, get_object_or_404, redirect
from loja.models import Produto, Carrinho, CarrinhoItem, Usuario
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.utils import timezone


# Função para adicionar um item ao carrinho
def create_carrinhoitem_view(request, produto_id=None):
    print('create_carrinhoitem_view')

    produto = get_object_or_404(Produto, pk=produto_id)
    if produto:
        print('produto:', produto.id)

    # Tenta pegar o carrinho da sessão ou cria um novo carrinho
    carrinho_id = request.session.get('carrinho_id')
    print('carrinho_id da sessão:', carrinho_id)

    carrinho = None
    if carrinho_id:
        carrinho = Carrinho.objects.filter(id=carrinho_id).first()
        if carrinho:
            print('Carrinho encontrado:', carrinho.id)
            hoje = datetime.today().date()

            if carrinho.criado_em.date() != hoje:
                carrinho = Carrinho.objects.create()
                request.session['carrinho_id'] = carrinho.id
                print('Carrinho antigo expirado, novo carrinho criado:', carrinho.id)
        else:
            carrinho = Carrinho.objects.create()
            request.session['carrinho_id'] = carrinho.id
            print('Carrinho inexistente recriado:', carrinho.id)
    else:
        carrinho = Carrinho.objects.create()
        request.session['carrinho_id'] = carrinho.id
        print('Novo carrinho criado:', carrinho.id)

    # Verifica se o produto já existe no carrinho
    carrinho_item = CarrinhoItem.objects.filter(carrinho=carrinho, produto=produto).first()

    if carrinho_item:
        carrinho_item.quantidade += 1
        print(f'Item do carrinho {carrinho_item.id}: quantidade incrementada.')
    else:
        carrinho_item = CarrinhoItem.objects.create(
            carrinho=carrinho,
            produto=produto,
            quantidade=1,
            preco=produto.preco
        )
        print('Novo item adicionado ao carrinho:', carrinho_item.id)

    carrinho_item.save()
    print('Item de carrinho salvo com sucesso:', carrinho_item.id)

    return redirect('/carrinho')


# Função para exibir os itens do carrinho
def list_carrinho_view(request):
    print('list_carrinho_view')

    carrinho = None
    carrinho_item = None

    carrinho_id = request.session.get('carrinho_id')

    if carrinho_id:
        print('carrinho_id da sessão:', carrinho_id)
        carrinho = Carrinho.objects.filter(id=carrinho_id).first()

        if carrinho:
            print('Data do carrinho:', carrinho.criado_em)
            carrinho_item = CarrinhoItem.objects.filter(carrinho_id=carrinho_id)

            if carrinho_item.exists():
                print('Itens de carrinho encontrados:', list(carrinho_item))
        else:
            print('Carrinho não encontrado no banco.')
    else:
        print('Nenhum carrinho na sessão.')

    context = {
        'carrinho': carrinho,
        'itens': carrinho_item
    }

    return render(request, 'carrinho/carrinho-listar.html', context)


# Função para confirmar o carrinho (compra)
@login_required
def confirmar_carrinho_view(request):
    print('confirmar_carrinho_view')

    carrinho_id = request.session.get('carrinho_id')
    carrinho = Carrinho.objects.filter(id=carrinho_id).first() if carrinho_id else None

    if carrinho:
        # Vincula o carrinho diretamente ao usuário logado
        carrinho.user = request.user  # <-- aqui é o objeto User do Django
        carrinho.situacao = 1
        carrinho.confirmado_em = timezone.now()
        carrinho.save()
        print('Carrinho confirmado e salvo com sucesso.')
    else:
        print('Nenhum carrinho para confirmar.')

    context = {
        'carrinho': carrinho
    }

    return render(request, 'carrinho/carrinho-confirmado.html', context)


# Função para excluir um item do carrinho
def remover_item_view(request, item_id):
    print('remover_item_view')

    item = get_object_or_404(CarrinhoItem, id=item_id)

    carrinho_id = request.session.get('carrinho_id')
    if carrinho_id == item.carrinho.id:
        item.delete()
        print(f'Item {item_id} removido do carrinho {carrinho_id}.')

    return redirect('/carrinho')
