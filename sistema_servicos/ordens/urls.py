from django.urls import path
from .views import listar_ordens, criar_ordem, mudar_status

urlpatterns = [
    path('', listar_ordens, name='ordem_lista'),
    path('nova/', criar_ordem, name='ordem_nova'),
    path('status/<int:id>/<str:status>/', mudar_status, name='ordem_status'),
]
