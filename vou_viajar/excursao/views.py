"""
Views da aplicação 'excursao'.
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.defaults import bad_request, server_error
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import json

from .models import Excursao, Destino, PrestadorServico, TipoPrestadorServico, Transporte, Orcamento, Roteiro

from .forms import PrestadorForm, TransporteForm, DestinoForm, ExcursaoForm, OrcamentoForm, RoteiroForm

from vou_viajar.conta.models import Pessoa, Agencia


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
def adicionar_transporte(request):
    form = TransporteForm()
    if request.method == 'POST':
        form = TransporteForm(request.POST)
        if form.is_valid():
            transporte = form.save(commit=False)
            transporte.agencia = get_agencia_usuario(request.user)
            transporte.save()
            messages.success(request, 'Transporte cadastrado com sucesso!')
            return redirect('adicionar_orcamento')
        else:
            messages.error(request, 'Formulário contém erros!!!')    
    
    return render(request, 'excursao/adicionar_transporte.html', {'form': form})


@login_required
def atualizar_transporte(request, pk):
    transporte = get_object_or_404(Transporte, pk=pk)
    form = TransporteForm(instance=transporte)
    if request.method == 'POST':
        form = TransporteForm(request.POST, instance=transporte)    
        if form.is_valid():
            transporte = form.save(commit=False)
            transporte.prestador_servico = form.cleaned_data['prestador_servico']
            transporte.modelo = form.cleaned_data['modelo']
            transporte.marca = form.cleaned_data['marca']
            transporte.ano = form.cleaned_data['ano']
            transporte.poltronas = form.cleaned_data['poltronas']
            transporte.banheiro = form.cleaned_data['banheiro']
            transporte.frigobar = form.cleaned_data['frigobar']
            transporte.ar_condicionado = form.cleaned_data['ar_condicionado']
            transporte.som = form.cleaned_data['som']
            transporte.tv = form.cleaned_data['tv']
            transporte.observacao = form.cleaned_data['observacao']                        
            transporte.save()
            messages.success(request, 'Sucesso')
            return redirect('listar_transporte')
        else:
            return render(request, 'excursao/atualizar_transporte.html', {'form': form, 'destino': transporte})
    
    elif request.method == 'GET':
        return render(request, 'excursao/atualizar_destino.html', {'form': form, 'destino': transporte})



@login_required
def listar_transporte(request):
    transportes = Transporte.objects.filter(agencia=get_agencia_usuario(request.user).pk)
    return render(request, 'excursao/listar_transporte.html', {'transportes': transportes})


@login_required
def deletar_transporte(request, pk):
    transporte = get_object_or_404(Transporte, pk=pk)
    if transporte.delete():
        return redirect('listar_transporte')
    else:
        return server_errror(request, 'ops_500.html')


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
 

def get_prestadores_servico_tipo(request, pk):
    prestadores = PrestadorServico.objects.filter(agencia=get_agencia_usuario(request.user).pk, categoria_id=pk)
    prestadores_dict = {}
    for prestador in prestadores:
        prestadores_dict[prestador.id] = prestador.nome
    return HttpResponse(json.dumps(prestadores_dict), content_type="application/json")


@login_required
def deletar_prestador_servico(request, pk):
    prestador = get_object_or_404(PrestadorServico, pk=pk)
    if prestador.delete():
        return redirect('listar_prestador_servico')
    else:
        return server_errror(request, 'ops_500.html')

@login_required
def adicionar_orcamento(request):
    form = OrcamentoForm()
    if request.method == 'POST':
        form = OrcamentoForm(request.POST)
        if form.is_valid():
            orcamento = form.save(commit=False)
            if Orcamento.objects.filter(nome=orcamento.nome).exists():
                messages.error(requests, 'Já existe um orçamento com este nome.')
            else:
                orcamento.agencia = get_agencia_usuario(request.user)
                orcamento.save()
                messages.success(request, 'Orçamento cadastrado com sucesso!')
                return redirect('listar_orcamento')
        else:
            messages.error(request, 'Formulário contém erros!!!')     
    return render(request, 'excursao/adicionar_orcamento.html', {'form': form})


@login_required
def atualizar_orcamento(request, pk):
    orcamento = get_object_or_404(Orcamento, pk=pk)
    form = OrcamentoForm(instance=orcamento)
    if request.method == 'POST':
        form = OrcamentoForm(request.POST, instance=orcamento)
        if form.is_valid():
            orcamento = form.save(commit=False)
            orcamento.excursao = form.cleaned_data['excursao']
            orcamento.tipo_prestador_servico = form.cleaned_data['tipo_prestador_servico']
            orcamento.prestador_servico = form.cleaned_data['prestador_servico']
            orcamento.cotacao = form.cleaned_data['cotacao']
            orcamento.horario_partida = form.cleaned_data['horario_partida']
            orcamento.horario_chegada = form.cleaned_data['horario_chegada']
            orcamento.selecionado = form.cleaned_data['selecionado']
            orcamento.observacao = form.cleaned_data['observacao']
            orcamento.save()
            messages.success(request, 'Sucesso')
            return redirect('listar_orcamento')
        else:
            return render(request, 'excursao/atualizar_orcamento.html', {'form': form, 'orcamento': orcamento})

    elif request.method == 'GET':
        return render(request, 'excursao/atualizar_orcamento.html', {'form': form, 'orcamento': orcamento})
                                 

@login_required
def listar_orcamento(request):
    orcamentos = Orcamento.objects.filter(agencia=get_agencia_usuario(request.user).pk)
    return render(request, 'excursao/listar_orcamento.html', {'orcamentos': orcamentos})


@login_required
def deletar_orcamento(request, pk):
    orcamento = get_object_or_404(Orcamento, pk=pk)
    if orcamento.delete():
        return redirect('listar_orcamento')
    else:
        return server_errror(request, 'ops_500.html')


@login_required
def adicionar_roteiro(request):
    form = RoteiroForm()
    if request.method == 'POST':
        form = RoteiroForm(request.POST)
        if form.is_valid():
            roteiro = form.save(commit=False)
            roteiro.agencia = get_agencia_usuario(request.user)
            roteiro.save()
            messages.success(request, 'Roteiro cadastrado com sucesso!')
            return redirect('listar_roteiro')
        else:
            messages.error(request, 'Formulário contém erros!')     
    return render(request, 'excursao/adicionar_roteiro.html', {'form': form})


@login_required
def atualizar_roteiro(request, pk):
    roteiro = get_object_or_404(Roteiro, pk=pk)
    form = RoteiroForm(instance=roteiro)
    if request.method == 'POST':
        form = RoteiroForm(request.POST, instance=roteiro)
        if form.is_valid():
            roteiro = form.save(commit=False)
            roteiro.excursao = form.cleaned_data['excursao']
            roteiro.horario_inicio = form.cleaned_data['horario_inicio']
            roteiro.horario_fim  = form.cleaned_data['horario_fim']
            roteiro.pago = form.cleaned_data['pago']
            roteiro.incluso = form.cleaned_data['incluso']
            roteiro.custo = form.cleaned_data['custo']
            roteiro.observacao = form.cleaned_data['observacao']
            roteiro.save()
            messages.success(request, 'Sucesso')
            return redirect('listar_roteiro')
        else:
            return render(request, 'excursao/atualizar_roteiro.html', {'form': form, 'roteiro': roteiro})

    elif request.method == 'GET':
        return render(request, 'excursao/atualizar_roteiro.html', {'form': form, 'roteiro': roteiro})
                                 

@login_required
def listar_roteiro(request):
    roteiros = Roteiro.objects.filter(agencia=get_agencia_usuario(request.user).pk)
    return render(request, 'excursao/listar_roteiro.html', {'roteiros': roteiros})


@login_required
def deletar_roteiro(request, pk):
    roteiro = get_object_or_404(Roteiro, pk=pk)
    if roteiro.delete():
        return redirect('listar_roteiro')
    else:
        return server_errror(request, 'ops_500.html')