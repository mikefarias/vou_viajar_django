"""
Views da aplicação 'conta'.
"""

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
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

    return render(request, 'conta/login.html')

def login_modal(request):
    """
    View para mostrar a tela de login do sistema.
    """

    return render(request, 'conta/login-modal.html')


def menu(request):
    """
    View para mostrar a tela de login do sistema.

    """
    return render(request, 'conta/menu.html')


def adicionar_agencia(request):
    """
    View para mostrar a tela de cadastro de uma agência e receber a requisição
    de cadastro.
    """

    form_agencia = None
    form_pessoa = None
    if request.method == 'POST':
        form = AgenciaForm(request.POST)
        if form.is_valid():
            agencia = form.save(commit=False)
            agencia.usuario_cadastro = request.user
            agencia.save()
            messages.success(request, 'Agência cadastrada com sucesso!')
            return redirect('home')
    else:
        form_agencia = AgenciaForm()
        form_pessoa = PessoaForm()
    return render(
        request,
        'conta/adicionar_agencia.html',
        {'form_agencia': form_agencia,'form_pessoa' : form_pessoa })

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('')
    template_name = 'registration/register.html'