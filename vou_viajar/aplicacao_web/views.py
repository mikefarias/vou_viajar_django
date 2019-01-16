from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from core.models import Evento
from core.models import Agencia
from core.forms import EventoForm
from core.forms import AgenciaForm

def home(request):
    return render(request, 'aplicacao_web/home.html')


def base(request):
    return render(request, 'base.html')


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'autenticacao/login.html')


def add_agency(request):
    if request.method == 'POST':
        agencia = Agencia()
        form = AgenciaForm(request.POST, instance=agencia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Agência cadastrada com sucesso!')
            return redirect('index')
        else:
            return render(request, 'aplicacao_web/add_agency.html', {'form': form})
    else:
        form = AgenciaForm()
        return render(request, 'aplicacao_web/add_agency.html', {'form': form})
