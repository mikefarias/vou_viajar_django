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

from .forms import TravelAgencyForm, ProfileForm, UserCreationForm, UserLoginForm
from .models import User, TravelAgency
from .tokens import account_activation_token  


def add_user(request):  
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
def add_agency(request):
    """
    View para mostrar a tela de cadastro de uma agência e receber a requisição
    de cadastro.
    """
    
    form_agency = None
    form_profile = None
    
    if request.method == 'POST':
        form_agency   = TravelAgencyForm(request.POST)
        form_profile  = ProfileForm(request.POST)
        if form_agency.is_valid() and form_profile.is_valid():
            agency = form_agency.save(commit=False)
            agency.user_registration = request.user
            agency.save()

            profile = form_profile.save(commit=False)
            profile.user = request.user
            profile.agency = agency
            form_profile.save()
            messages.success(request, 'Agência cadastrada com sucesso!')
            return redirect('home')
    else:
        form_agency  = TravelAgencyForm()
        form_profile = ProfileForm()
    return render(
        request,
        'conta/adicionar_agencia.html',
        {'form_agency': form_agency,'form_profile' : form_profile })


def update_agency(request, pk):
    agency = get_object_or_404(TravelAgency, pk=pk)
    form_agency = TravelAgencyForm(instance=agency)

    if request.method == 'POST':
        form = TravelAgencyForm(request.POST, instance=agency)    
        if form.is_valid():
            agency = form.save(commit=False)
            agency.code_cadastur = form.cleaned_data['code_cadastur']
            agency.cnpj = form.cleaned_data['cnpj']
            agency.physical_agency = form.cleaned_data['physical_agency']
            agency.address = form.cleaned_data['address']
            agency.logo = form.cleaned_data['logo']
            agency.owner_id = form.cleaned_data['owner_id']
            agency.save()
            messages.success(request, 'Agência atualizado!')
            return redirect('home')
        else:
            return render(request, 'conta/update_agency.html', {'form_agency': form_agency, 'agency': agency})
    
    elif request.method == 'GET':
        return render(request, 'conta/update_agency.html', {'form_agency': form_agency, 'agency': agency})