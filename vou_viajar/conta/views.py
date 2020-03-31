"""
Views da aplicação 'conta'.
"""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.sites.shortcuts import get_current_site 
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse 
from django.utils.encoding import force_bytes, force_text  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from .forms import AgenciaForm, PessoaForm, UserCreationForm, UserLoginForm
from .models import User, Agencia, Pessoa
from .tokens import account_activation_token  


def cadastrar_usuario(request):  
    if request.method == 'POST':  
        form_usuario = UserCreationForm(request.POST) 
        if form_usuario.is_valid():  
            user = form_usuario.save(commit=False)  
            user.is_active = False  
            user.save()  
            current_site = get_current_site(request)  
            mail_subject = 'Activate your account.'  
            message = render_to_string('registration/ativar_conta_email.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid': urlsafe_base64_encode(force_bytes(user.id)).decode(),  
                'token': account_activation_token.make_token(user),  
            })  
            to_email = form_usuario.cleaned_data.get('email')  
            email = EmailMessage(  
            mail_subject, message, to=[to_email]  
            )  
            email.send()  
            return HttpResponse('Please confirm your email address to complete the registration')
        else:
            messages.error(request, form_usuario.errors)  
    else:  
        form_usuario = UserCreationForm()
    return render(request, 'registration/register.html', {'form_usuario': form_usuario})

        
def activate(request, uidb64, token):  
    
    uid = force_text(urlsafe_base64_decode(uidb64))  
    user = User.objects.get(id=uid)  
      
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    else:  
        return HttpResponse('Activation link is invalid!')


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
            messages.error(request, 'Email e/ou senha incorreto(s)!')
    else:
        form_login = UserLoginForm()

    return render(request, 'registration/login.html', {'form_login': form_login})

def logout_view(request):
    logout(request)
    messages.info(request, 'Logout realizado com sucesso!')
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
            return redirect('home')
    else:
        form_agencia = AgenciaForm()
        form_pessoa = PessoaForm()
    return render(
        request,
        'conta/adicionar_agencia.html',
        {'form_agencia': form_agencia,'form_pessoa' : form_pessoa })


def atualizar_agencia(request, pk):
    agencia = get_object_or_404(Agencia, pk=pk)
    form_agencia = AgenciaForm(instance=agencia)

    if request.method == 'POST':
        form = AgenciaForm(request.POST, instance=agencia)    
        if form.is_valid():
            agencia = form.save(commit=False)
            agencia.nome_fantasia = form.cleaned_data['nome_fantasia']
            agencia.nome_juridico = form.cleaned_data['nome_juridico']
            agencia.cod_cadastur = form.cleaned_data['cod_cadastur']
            agencia.cnpj = form.cleaned_data['cnpj']
            agencia.agencia_fisica = form.cleaned_data['agencia_fisica']
            agencia.foto_perfil = form.cleaned_data['foto_perfil']
            agencia.save()
            messages.success(request, 'Agência atualizado!')
            return redirect('home')
        else:
            return render(request, 'conta/atualizar_agencia.html', {'form_agencia': form_agencia, 'agencia': agencia})
    
    elif request.method == 'GET':
        return render(request, 'conta/atualizar_agencia.html', {'form_agencia': form_agencia, 'agencia': agencia})
