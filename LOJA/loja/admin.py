from django.contrib import admin
# Register your models here.
from .models import *
class FabricanteAdmin(admin.ModelAdmin):
    # Cria um filtro de hierarquia com datas
    date_hierarchy = 'criado_em'
class ProdutoAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    list_display = ('Produto', 'destaque', 'promocao', 'preco', 'categoria',)
    fields = ('Produto', 'destaque', 'promocao', 'preco', 'categoria',)
    search_fields = ('Produto',)
    exclude = ('msgPromocao',)
    empty_value_display = 'Vazio'
admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)