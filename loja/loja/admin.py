from django.contrib import admin
from .models import Categoria, Produto, Fabricante

class FabricanteAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'

class ProdutoAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    list_display = ('Produto', 'preco', 'categoria')  # Campos a serem exibidos na lista
    empty_value_display = 'Vazio'  # Valor exibido quando o campo estiver vazio
    fields = ('nome', 'destaque', 'promocao', 'preco', 'categoria')  # Campos a serem exibidos no formulário
    search_fields = ('nome', 'msgPromocao')  # Campos que podem ser usados para pesquisa

admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Fabricante, FabricanteAdmin)
