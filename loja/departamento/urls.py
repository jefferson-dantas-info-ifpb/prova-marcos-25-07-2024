from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("ferramentas", views.ferramentas),
    path("sem-estoque", views.sem_estoque),
    path("informatica/sem-estoque", views.informatica_sem_estoque),
    path("leves", views.leves),
    path("todos", views.todos_produtos),
]
