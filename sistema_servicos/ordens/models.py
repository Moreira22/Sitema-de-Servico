from django.db import models
from clientes.models import Cliente
from servicos.models import Servico

class OrdemServico(models.Model):
    STATUS_CHOICES = [
        ('ABERTA', 'Aberta'),
        ('EM_ANDAMENTO', 'Em andamento'),
        ('FINALIZADA', 'Finalizada'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicos = models.ManyToManyField(Servico)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ABERTA')
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"OS #{self.id} - {self.cliente.nome}"
