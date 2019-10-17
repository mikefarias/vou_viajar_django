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
from .models import PrestadorServico
from .forms import PrestadorForm
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
    if request.method == 'POST':
        form = ExcursaoForm(request.POST, instance=excursao)    
        if form.is_valid():
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
    
    elif request.method == 'GET':
        return render(request, 'excursao/atualizar_excursao.html', {'form': form, 'excursao' : excursao})


@login_required
def deletar_excursao(request, pk):
    excursao = get_object_or_404(Excursao, pk=pk)
    if excursao.delete():
        return redirect('../listar')
    else:
        return server_errror(request, 'ops_500.html')
    return render(request, '/../listar.html', {'excursoes': excursoes})


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
            return redirect('listar_excursao')
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
    if request.method == 'POST':
        form = DestinoForm(request.POST, instance=destino)    
        if form.is_valid():
            destino = form.save(commit=False)
            destino.nome_turistico = form.cleaned_data['nome_turistico']
            destino.pais = form.cleaned_data['pais']
            destino.estado = form.cleaned_data['estado']
            destino.cidade_fim = form.cleaned_data['cidade']
            destino.cep = form.cleaned_data['cep']
            destino.save()
            messages.success(request, 'Sucesso')
            return redirect('listar_destino')
        else:
            return render(request, 'excursao/atualizar_destino.html', {'form': form, 'destino': destino})
    
    elif request.method == 'GET':
        return render(request, 'excursao/atualizar_destino.html', {'form': form, 'destino': destino})


@login_required
def deletar_destino(request, pk):
    destino = get_object_or_404(Destino, pk=pk)
    if destino.delete():
        return redirect('listar_destino')
    else:
        return server_errror(request, 'ops_500.html')


def get_agencia_usuario(usuario):
    pessoa = Pessoa.objects.get(usuario=usuario)
    agencia = Agencia.objects.get(pessoa=pessoa)
    return agencia


@login_required
def adicionar_orcamento(request): 
    
    form = None
    if request.method == 'POST':
        form = PrestadorForm(request.POST)
        if form.is_valid():
            prestador = form.save(commit=False)
            prestador.agencia = get_agencia_usuario(request.user)
            prestador.save()
            messages.success(request, 'Prestador de Serviço cadastrado com sucesso!')
            return redirect('listar_orcamento')
    else:
        form = PrestadorForm()
    return render(request, 'excursao/adicionar_orcamento.html', {'form': form})

@login_required
def atualizar_orcamento(request, pk):
    pass


@login_required
def listar_orcamento(request):
    orcamentos = PrestadorServico.objects.filter(agencia=get_agencia_usuario(request.user).pk)
    return render(request, 'excursao/listar_orcamento.html', {'orcamentos': orcamentos})


@login_required
def deletar_orcamento(request, pk):
    pass


@login_required
def adicionar_prestador_servico(request):
    form = None
    if request.method == 'POST':
        form = PrestadorForm(request.POST)
        if form.is_valid():
            prestador = form.save(commit=False)
            prestador.agencia = get_agencia_usuario(request.user)
            prestador.save()
            messages.success(request, 'Prestador de Serviço cadastrado com sucesso!')
            return redirect('listar_prestador_servico')
    else:
        form = PrestadorForm()
    return render(request, 'excursao/adicionar_prestador_servico.html', {'form': form})


@login_required
def atualizar_prestador_servico(request, pk):
    prestador= get_object_or_404(PrestadorServico, pk=pk)
    form = PrestadorForm(instance=prestador)
    if request.method == 'POST':
        form = PrestadorForm(request.POST, instance=prestador)
        if form.is_valid():
            prestador = form.save(commit=False)
            prestador.nome = form.cleaned_data['nome']
            prestador.cnpj_cpf = form.cleaned_data['cnpj_cpf']
            prestador.pessoa_juridica = form.cleaned_data['pessoa_juridica']
            prestador.cadastur = form.cleaned_data['cadastur']
            prestador.email = form.cleaned_data['email']
            prestador.telefone = form.cleaned_data['telefone']
            prestador.endereco = form.cleaned_data['endereco']
            prestador.horario_funcionamento = form.cleaned_data['horario_funcionamento']
            prestador.save()
            messages.success(request, 'Sucesso')
            return redirect('listar_prestador_servico')
        else:
            return render(request, 'excursao/atualizar_prestador_servico.html', {'form': form, 'prestador': prestador})

    elif request.method == 'GET':
        return render(request, 'excursao/atualizar_prestador_servico.html', {'form': form, 'prestador': prestador})


@login_required
def listar_prestador_servico(request):
    prestadores = PrestadorServico.objects.filter(agencia=get_agencia_usuario(request.user).pk)
    return render(request, 'excursao/listar_prestador_servico.html', {'prestadores': prestadores})


@login_required
def deletar_prestador_servico(request, pk):
    prestador = get_object_or_404(PrestadorServico, pk=pk)
    if prestador.delete():
        return redirect('listar_prestador_servico')
    else:
        return server_errror(request, 'ops_500.html')