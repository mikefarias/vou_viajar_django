from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from core.models import Excursao
from core.models import Agencia
from core.forms import ExcursaoForm
from core.forms import AgenciaForm

def home(request):
    return render(request, 'aplicacao_web/home.html')


def base(request):
    return render(request, 'base.html')


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'autenticacao/login.html')


def adicionar_agencia(request):
    if request.method == 'POST':
        agencia = Agencia()
        form = AgenciaForm(request.POST, instance=agencia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Agência cadastrada com sucesso!')
            return redirect('index')
        else:
            return render(request, 'aplicacao_web/adicionar_agencia.html', {'form': form})
    else:
        form = AgenciaForm()
        return render(request, 'aplicacao_web/adicionar_agencia.html', {'form': form})


def adicionar_excursao(request):
    if request.method == 'POST':
        excursao = Excursao()
        form = ExcursaoForm(request.POST, instance=excursao)
        if form.is_valid():
            form.save()
            messages.success(request, 'Excursão cadastrada com sucesso!')
            return redirect('index')
        else:
            return render(request, 'aplicacao_web/adicionar_excursao.html', {'form': form})
    else:
        form = ExcursaoForm()
        return render(request, 'aplicacao_web/adicionar_excursao.html', {'form': form})

