from django.db import models

# Create your models here.
class Produto(models.Model):
    categoria = models.CharField(max_length=100)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(decimal_places=2, max_digits=10)
    quantidade = models.IntegerField()
    peso = models.IntegerField()

    def __str__(self):
        return f'{self.categoria} / {self.nome} / {self.quantidade}'
