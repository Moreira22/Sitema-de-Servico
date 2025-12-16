from django.urls import path
from .views import (
    listar_clientes,
    criar_cliente,
    editar_cliente,
    excluir_cliente
)

urlpatterns = [
    path('', listar_clientes, name='cliente_lista'),
    path('novo/', criar_cliente, name='cliente_novo'),
    path('editar/<int:id>/', editar_cliente, name='cliente_editar'),
    path('excluir/<int:id>/', excluir_cliente, name='cliente_excluir'),
]
