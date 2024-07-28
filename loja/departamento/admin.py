from django.contrib import admin
from .models import Produto

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'categoria', 'nome', 'preco', 'quantidade', 'peso')

# Register your models here.
admin.site.register(Produto, ProdutoAdmin)
