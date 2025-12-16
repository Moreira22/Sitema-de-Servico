from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cliente

@login_required
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/list.html', {'clientes': clientes})


@login_required
def criar_cliente(request):
    if request.method == 'POST':
        Cliente.objects.create(
            nome=request.POST['nome'],
            documento=request.POST['documento']
        )
        return redirect('/clientes/')

    return render(request, 'clientes/form.html')

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        cliente.nome = request.POST['nome']
        cliente.documento = request.POST['documento']
        cliente.save()
        return redirect('cliente_lista')

    return render(request, 'clientes/form.html', {
        'cliente': cliente
    })

def excluir_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        cliente.delete()

    return redirect('cliente_lista')
