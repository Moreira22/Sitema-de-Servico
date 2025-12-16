from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Servico

@login_required
def listar_servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'servicos/list.html', {'servicos': servicos})


@login_required
def criar_servico(request):
    if request.method == 'POST':
        Servico.objects.create(
            nome=request.POST['nome'],
            preco=request.POST['preco']
        )
        return redirect('/servicos/')

    return render(request, 'servicos/form.html')
