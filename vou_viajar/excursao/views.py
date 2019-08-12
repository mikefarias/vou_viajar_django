"""
Views da aplicação 'excursao'.
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.defaults import bad_request, server_error
from django.contrib import messages
from django.http import HttpResponseRedirect
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
def atualizar_excursao(request, pk):
    excursao = get_object_or_404(Excursao, pk=pk)
    form = ExcursaoForm(instance=excursao)
    if(request.method == 'POST'):
        form = ExcursaoForm(request.POST, instance=excursao)    
        if(form.is_valid()):
            excursao = form.save(commit=False)
            excursao.titulo = form.cleaned_data['titulo']
            excursao.descricao = form.cleaned_data['descricao']
            excursao.horario_inicio = form.cleaned_data['horario_inicio']
            excursao.horario_fim = form.cleaned_data['horario_fim']
            excursao.origem = form.cleaned_data['origem']
            excursao.destino = form.cleaned_data['destino']
            excursao.save()
            messages.success(request, _("Sucesso"))
            return redirect('../listar')
        else:
            return render(request, 'excursao/atualizar_excursao.html', {'form': form, 'excursao' : excursao})
    
    elif(request.method == 'GET'):
        return render(request, 'excursao/atualizar_excursao.html', {'form': form, 'excursao' : excursao})

@login_required
def deletar_excursao(request, pk):
    excursao = get_object_or_404(Excursao, pk=pk)
    if excursao.delete():
        return redirect('../listar_excursao')
    else:
        return server_errror(reqest, 'ops_500.html')

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
            return redirect('listar')
    else:
        form = ExcursaoForm()
    return render(
        request,
        'excursao/adicionar_excursao.html',
        {'form': form},
    )
