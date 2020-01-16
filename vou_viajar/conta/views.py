"""
Views da aplicação 'conta'.
"""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import AgenciaForm
from .forms import PessoaForm
from .forms import UserCreationForm, UserLoginForm

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('login_view')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'registration/register.html', {'form_usuario': form_usuario})

def login_view(request):
    if request.method == 'POST':
        form_login = UserLoginForm(request.POST)
        email = request.POST["email"]
        password = request.POST["password"]
        usuario = authenticate(request, email=email, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('home')
        else:
            messages.success(request, 'Não foi possível realizar a autenticação')
    else:
        form_login = UserLoginForm()

    return render(request, 'registration/login.html', {'form_login': form_login})

def logout_view(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'Logout realizado com sucesso!')
    return redirect('/')

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