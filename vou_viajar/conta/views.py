"""
Views da aplicação 'conta'.
"""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import AgenciaForm
from .forms import PessoaForm

# Create your views here.

def login(request):
    """
    View para mostrar a tela de login do sistema.
    """
    return render(request, 'registration/login.html')

@login_required
def menu(request):
    """
    View para mostrar a tela de login do sistema.

    """
    messages.add_message(request, messages.INFO, 'Menu de Excursões')
    return render(request, 'conta/menu.html')

@login_required
def adicionar_agencia(request):
    """
    View para mostrar a tela de cadastro de uma agência e receber a requisição
    de cadastro.
    """
    
    form_agencia = None
    form_pessoa = None
    if request.method == 'POST':
        form_agencia= AgenciaForm(request.POST)
        form_pessoa = PessoaForm(request.POST)
        if form_agencia.is_valid() and form_pessoa.is_valid():
            agencia = form_agencia.save(commit=False)
            agencia.usuario_cadastro = request.user
            agencia.save()

            pessoa = form_pessoa.save(commit=False)
            pessoa.usuario = request.user
            pessoa.agencia = agencia
            form_pessoa.save()
            messages.success(request, 'Agência cadastrada com sucesso!')
            return redirect('conta_menu')
    else:
        form_agencia = AgenciaForm()
        form_pessoa = PessoaForm()
    return render(
        request,
        'conta/adicionar_agencia.html',
        {'form_agencia': form_agencia,'form_pessoa' : form_pessoa })

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    