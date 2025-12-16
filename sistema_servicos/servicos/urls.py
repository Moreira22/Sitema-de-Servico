from django.urls import path
from .views import listar_servicos, criar_servico

urlpatterns = [
    path('', listar_servicos),
    path('novo/', criar_servico),
]
