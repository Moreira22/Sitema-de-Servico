from django.urls import path
from .views import listar_ordens, criar_ordem

urlpatterns = [
    path('', listar_ordens),
    path('nova/', criar_ordem),
]
