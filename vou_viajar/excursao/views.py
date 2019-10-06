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
from .models import Destino
from .forms import DestinoForm
from vou_viajar.conta.models import Pessoa
from vou_viajar.conta.models import Agencia
@login_required
def menu_excursao(request):
    return render(request, 'excursao/menu_excursao.html')

@login_required
def listar_excursao(request):
    excursoes = Excursao.objects.filter(agencia=get_agencia_usuario(request.user).pk)
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
            excursao.save()
            form.save_m2m()
            return redirect('../listar')
        else:
            return render(request, 'excursao/atualizar_excursao.html', {'form': form, 'excursao' : excursao})
    
    elif(request.method == 'GET'):
        return render(request, 'excursao/atualizar_excursao.html', {'form': form, 'excursao' : excursao})

@login_required
def deletar_excursao(request, pk):
    excursao = get_object_or_404(Excursao, pk=pk)
    if excursao.delete():
        return redirect('../listar')
    else:
        return server_errror(request, 'ops_500.html')

    return render(request, 'excursao/listar.html', {'excursoes': excursoes})

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
            excursao.agencia = get_agencia_usuario(request.user)
            excursao.save()
            form.save_m2m()
            messages.success(request, 'Excursão cadastrada com sucesso!')
            return redirect('listar')
    else:
        form = ExcursaoForm()
    return render(
        request,
        'excursao/adicionar_excursao.html',
        {'form': form},
    )

@login_required
def adicionar_destino(request):
    """
    View para mostrar a tela de mapeamento de um excursão e receber a requisição
    de cadastro.
    """

    form = None
    if request.method == 'POST':
        form = DestinoForm(request.POST)
        if form.is_valid():
            destino = form.save(commit=False)
            destino.agencia = get_agencia_usuario(request.user)
            destino.save()
            messages.success(request, 'Destino mapeado com sucesso!')
            return redirect('listar_destino')
    else:
        form = DestinoForm()
    return render(
        request,
        'excursao/adicionar_destino.html',
        {'form': form},
    )

@login_required
def listar_destino(request):
    destinos = Destino.objects.filter(agencia=get_agencia_usuario(request.user).pk)
    return render(request, 'excursao/listar_destino.html', {'destinos': destinos})

@login_required
def atualizar_destino(request, pk):
    destino = get_object_or_404(Destino, pk=pk)
    form = DestinoForm(instance=destino)
    if(request.method == 'POST'):
        form = DestinoForm(request.POST, instance=destino)    
        if(form.is_valid()):
            destino = form.save(commit=False)
            destino.nome_turistico = form.cleaned_data['nome_turistico']
            destino.pais = form.cleaned_data['pais']
            destino.estado = form.cleaned_data['estado']
            destino.cidade_fim = form.cleaned_data['cidade']
            destino.cep = form.cleaned_data['cep']
            destino.save()
            messages.success(request,('Sucesso'))
            return redirect('../listar')
        else:
            return render(request, 'excursao/atualizar_destino.html', {'form': form, 'destino' : destino})
    
    elif(request.method == 'GET'):
        return render(request, 'excursao/atualizar_destino.html', {'form': form, 'destino' : destino})

@login_required
def deletar_destino(request, pk):
    destino = get_object_or_404(Destino, pk=pk)
    if destino.delete():
        return redirect('../listar')
    else:
        return server_errror(request, 'ops_500.html')

    return render(request, 'excursao/listar_destino.html', {'destinos': destinos})

def get_agencia_usuario(usuario):
    pessoa = Pessoa.objects.get(usuario=usuario)
    agencia = Agencia.objects.get(pessoa=pessoa)
    return agencia