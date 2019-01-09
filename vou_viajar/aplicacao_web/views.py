from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from core.forms import EventoForm
from core.models import Evento


def home(request):
    return render(request, 'aplicacao_web/home.html')


def base(request):
    return render(request, 'base.html')


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'autenticacao/login.html')

def add_event(request):
    if request.method == 'POST':
        evento = Evento()
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evento cadastrado com sucesso!')
            return redirect('home')
        else:
            return render(request, 'evento.html', {'form': form})
    else:
        form = EventoForm()
        return render(request, 'evento.html', {'form': form})