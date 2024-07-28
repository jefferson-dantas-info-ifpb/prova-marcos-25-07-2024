from django.shortcuts import render
from .models import Produto

# Create your views here.
def ferramentas(request):
    produtos = Produto.objects.filter(categoria="Ferramentas")
    return render(request, 'produtos.html', {'titulo': 'Ferramentas', 'produtos': produtos})

def sem_estoque(request):
    produtos = Produto.objects.filter(quantidade=0)
    return render(request, 'produtos.html', {'titulo': 'Produtos em falta no estoque', 'produtos': produtos})

def informatica_sem_estoque(request):
    produtos = Produto.objects.filter(quantidade=0, categoria="Informática")
    return render(request, 'produtos.html', {'titulo': 'Produtos de Informática em falta no estoque', 'produtos': produtos})

def leves(request):
    produtos = Produto.objects.filter(peso__gte=100, peso__lte=1000)
    return render(request, 'produtos.html', {'titulo': 'Produtos leves (100g - 1000g)', 'produtos': produtos})

def todos_produtos(request):
    produtos = Produto.objects.all()[:5]
    return render(request, 'produtos.html', {'titulo': '5 produtos', 'produtos': produtos})
