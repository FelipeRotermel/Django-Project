from django.contrib import admin

from livraria.models import Autor, Categoria, Editora, Livro, Compra, ItensCompra

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Livro)
admin.site.register(Compra)
admin.site.register(ItensCompra)