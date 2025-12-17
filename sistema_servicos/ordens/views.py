from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import OrdemServico
from clientes.models import Cliente
from servicos.models import Servico

@login_required
def listar_ordens(request):
    ordens = OrdemServico.objects.all()
    return render(request, 'ordens/list.html', {'ordens': ordens})


@login_required
def criar_ordem(request):
    clientes = Cliente.objects.all()
    servicos = Servico.objects.all()

    if request.method == 'POST':
        cliente_id = request.POST['cliente']
        servicos_ids = request.POST.getlist('servicos')

        ordem = OrdemServico.objects.create(
            cliente_id=cliente_id
        )

        ordem.servicos.set(servicos_ids)
        return redirect('/ordens/')

    return render(request, 'ordens/form.html', {
        'clientes': clientes,
        'servicos': servicos
    })


def mudar_status(request, id, status):
    ordem = get_object_or_404(OrdemServico, id=id)

    if status in ['ABERTA', 'ANDAMENTO', 'FINALIZADA']:
        ordem.status = status
        ordem.save()

    return redirect('ordem_lista')
