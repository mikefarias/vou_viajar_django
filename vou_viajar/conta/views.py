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
from django.http import HttpResponse, HttpResponseRedirect 
from django.utils.encoding import force_bytes, force_text  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string

from decouple import config
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from .forms import TravelAgencyForm, ContactTravelAgencyForm, ProfileForm, UserCreationForm, UserLoginForm
from .models import User, TravelAgency, ContactTravelAgency, Profile
from .tokens import account_activation_token  


def add_user(request):  
    if request.method == 'POST':  
        form_usuario = UserCreationForm(request.POST) 
        if form_usuario.is_valid():  
            user = form_usuario.save(commit=False)  
            user.is_active = False  
            user.save()  
            current_site = get_current_site(request)  
            mail_subject = 'Ative sua conta!.'  
            message = render_to_string('registration/ativar_conta_email.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid': urlsafe_base64_encode(force_bytes(user.id)).decode(),  
                'token': account_activation_token.make_token(user),  
            })  
            to_email = form_usuario.cleaned_data.get('email')  
            try:
                message = Mail(
                    from_email= config('DEFAULT_FROM_EMAIL'),
                    to_emails=to_email,
                    subject=mail_subject,
                    html_content=message)
                sg = SendGridAPIClient(config('SENDGRID_API_KEY'))
                response = sg.send(message)
            except Exception as e:
                print(e)    

            messages.info(request, 'Confirme em seu e-mail para concluir o registro')
            return redirect('login_view')  
        else:
            messages.error(request, form_usuario.errors) 
            return redirect('add_user') 
    else:  
        form_usuario = UserCreationForm()
    return render(request, 'registration/register.html', {'form_usuario': form_usuario})

        
def activate(request, uidb64, token):  
    
    uid     = force_text(urlsafe_base64_decode(uidb64))  
    user    = User.objects.get(id=uid)  
      
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()
        messages.success(request, 'Agradecemos sua confirmação por e-mail. Agora você pode acessar sua conta')    
        return redirect('login_view')
    else:  
        messages.error(request, 'O link está inválido!')
        return redirect('add_user')

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
    form_contact_agency = None
    
    if request.method == 'POST':
        form_agency = TravelAgencyForm(request.POST, request.FILES)
        form_contact_agency  = ContactTravelAgencyForm(request.POST)
        if form_agency.is_valid() and form_contact_agency.is_valid():
            contact_agency = form_contact_agency.save(commit=False)
            contact_agency.active = True
            contact_agency.save()
            agency = form_agency.save(commit=False)
            agency.owner = request.user
            agency.contact = contact_agency
            agency.active = True
            agency.save()
            messages.success(request, 'Agência cadastrada com sucesso!')
            return redirect('home')
        else:
            messages.error(request, form_agency.errors)
            print(form_agency.errors)
            return redirect('add_agency')
    else:
        form_agency  = TravelAgencyForm()
        form_contact_agency = ContactTravelAgencyForm()
    return render(
        request,
        'conta/add_agency.html',
        {'form_agency': form_agency,'form_contact_agency' : form_contact_agency })

@login_required
def update_agency(request, pk):
    agency = TravelAgency.objects.get(owner_id=pk)
    form_agency = TravelAgencyForm(instance=agency)

    contact_agency = agency.contact
    form_contact_agency = ContactTravelAgencyForm(instance=contact_agency)

    if request.method == 'POST':
        form_agency = TravelAgencyForm(request.POST, request.FILES, instance=agency)
        form_contact_agency = ContactTravelAgencyForm(request.POST, instance=contact_agency)       
        if form_contact_agency.is_valid():

            contact_agency              = form_contact_agency.save(commit=False)
            contact_agency.email        = form_contact_agency.cleaned_data['email']
            contact_agency.phone_number = form_contact_agency.cleaned_data['phone_number']
            contact_agency.whatsapp     = form_contact_agency.cleaned_data['whatsapp']
            contact_agency.fan_page     = form_contact_agency.cleaned_data['fan_page']
            contact_agency.instagram    = form_contact_agency.cleaned_data['instagram']
            contact_agency.website      = form_contact_agency.cleaned_data['website']
            contact_agency.save() 

            agency                  = form_agency.save(commit=False)
            agency.code_cadastur    = form_agency.cleaned_data['code_cadastur']
            agency.cnpj             = form_agency.cleaned_data['cnpj']
            agency.physical_agency  = form_agency.cleaned_data['physical_agency']
            agency.address          = form_agency.cleaned_data['address']
            agency.logo             = form_agency.cleaned_data['logo']
            agency.save()

            messages.success(request, 'Agência atualizada!')
            return redirect('home')
        else:
            print("Erros agencia", form_agency.errors)
            print("Erros contato", form_contact_agency.errors)
            return render(request, 'conta/update_agency.html', {'form_agency': form_agency, 'form_contact_agency': form_contact_agency})
    
    elif request.method == 'GET':
        return render(request, 'conta/update_agency.html', {'form_agency': form_agency, 'form_contact_agency': form_contact_agency})


@login_required
def add_profile(request):
    
    form_profile = None    
    if request.method == 'POST':
        form_profile = ProfileForm(request.POST, request.FILES)
        if form_profile.is_valid():    
            profile = form_profile.save(commit=False)
            profile.active = True
            profile.user = request.user
            profile.travel_agency = get_travel_agency(request.user)
            profile.save()
            messages.success(request, 'Perfil cadastrado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, form_profile.errors)
            return redirect('add_profile')
    else:
        form_profile  = ProfileForm()
    return render(
        request,
        'conta/add_profile.html',
        {'form_profile': form_profile })


@login_required
def update_profile(request, pk):
    profile = Profile.objects.get(user_id = pk)
    form_profile = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)    
        if form.is_valid():
            profile = form.save(commit=False)
            profile.cpf_cnpj      = form.cleaned_data['cpf_cnpj']
            profile.profile_photo = form.cleaned_data['profile_photo']
            profile.phone_number  = form.cleaned_data['phone_number']
            profile.whatsapp      = form.cleaned_data['whatsapp']
            profile.save()
            messages.success(request, 'Perfil atualizado!')
            return redirect('home')
        else:
            return render(request, 'conta/update_profile.html', {'form_profile': form_profile} )
    
    elif request.method == 'GET':
        return render(request, 'conta/update_profile.html', {'form_profile': form_profile} )


@login_required
def add_user_staff(request):  
    
    if request.method == 'POST':  
        form_user_staff = UserCreationForm(request.POST) 
        form_profile    = ProfileForm(request.POST, request.FILES)
        
        if form_user_staff.is_valid() and form_profile.is_valid():  
            
            user_staff              = form_user_staff.save(commit=False)  
            user_staff.is_active    = False  
            user_staff.save()  
            
            profile                 = form_profile.save(commit=False)
            profile.travel_agency   = get_travel_agency(request.user)
            profile.user            = user_staff
            profile.active          = True
            profile.save()
            
            current_site = get_current_site(request)  
            mail_subject = 'Ative sua conta!.'  
            message = render_to_string('registration/ativar_conta_email.html', {  
                'user': user_staff,  
                'domain': current_site.domain,  
                'uid': urlsafe_base64_encode(force_bytes(user_staff.id)).decode(),  
                'token': account_activation_token.make_token(user_staff),  
            })  
            to_email = form_user_staff.cleaned_data.get('email')  
            try:
                message = Mail(
                    from_email= config('DEFAULT_FROM_EMAIL'),
                    to_emails=to_email,
                    subject=mail_subject,
                    html_content=message)
                sg = SendGridAPIClient(config('SENDGRID_API_KEY'))
                response = sg.send(message)
            except Exception as e:
                print(e)    

            messages.info(request, 'Funcionário cadastrado. O mesmo precisa ativar registro através do e-mail.')
            return redirect('add_user_staff')  
        else:
            messages.error(request, form_user_staff.errors) 
            messages.error(request, form_profile.errors)
            return redirect('add_user_staff') 
    else:  
        form_user_staff = UserCreationForm()
        form_profile = ProfileForm()
    return render(request, 'conta/add_user_staff.html', {'form_user_staff': form_user_staff, 'form_profile': form_profile})


def get_travel_agency(user):
    agency = TravelAgency.objects.get(owner=user)
    return agency