"""
Views da aplicação 'excursao'.
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib import messages

from .models import Excursao
from .forms import ExcursaoForm

@login_required
def menu_excursao(request):
    return render(request, 'excursao/menu_excursao.html')

@login_required
def listar_excursao(request):
    excursoes = Excursao.objects.all()
    return render(request, 'excursao/listar_excursao.html', {'excursoes': excursoes})

@login_required
def adicionar_excursao(request):
    """
    View para mostrar a tela de cadastro de uma excursão e receber a requisição
    de cadastro.
    """

    form = None
    if request.method == 'POST':
        form = ExcursaoForm(request.POST)
        if form.is_valid():
            excursao = form.save(commit=False)
            excursao.usuario_cadastro = request.user
            excursao.save()
            messages.success(request, 'Excursão cadastrada com sucesso!')
            return redirect('listar_excursao.html')
    else:
        form = ExcursaoForm()
    return render(
        request,
        'excursao/adicionar_excursao.html',
        {'form': form},
    )
