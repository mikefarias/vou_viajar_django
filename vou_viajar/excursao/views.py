"""
Views da aplicação 'excursao'.
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.views.defaults import bad_request, server_error
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import json

from .models import Excursion, Destiny, ServiceProvider, ServiceProviderType
from .models import Transport, Estimate, TravelAgency, TravelItinerary

from .forms import ServiceProviderForm, TransportForm, DestinyForm, ExcursionForm, EstimateForm, TravelItineraryForm

from vou_viajar.conta.models import Profile, TravelAgency


@login_required
def home(request):
    return render(request, 'excursao/base_home.html')


@login_required
def listar_excursao(request):
    excursions = Excursion.objects.filter(travel_agency=get_agency_user(request.user).pk)
    return render(request, 'excursao/listar_excursao.html', {'excursions': excursions})


@login_required
def atualizar_excursao(request, pk):
    excursion = get_object_or_404(Excursion, pk=pk)
    form = ExcursionForm(instance=excursion)
    if request.method == 'POST':
        form = ExcursionForm(request.POST, instance=excursion)    
        if form.is_valid():
            excursion               = form.save(commit=False)
            excursion.name          = form.cleaned_data['name']
            excursion.details       = form.cleaned_data['details']
            excursion.origin        = form.cleaned_data['origin']
            excursion.start_time    = form.cleaned_data['start_time']
            excursion.end_time      = form.cleaned_data['end_time']
            excursion.save()
            form.save_m2m()
            return redirect('../listar')
        else:
            return render(request, 'excursao/atualizar_excursao.html', {'form': form, 'excursion' : excursion})
    
    elif request.method == 'GET':
        return render(request, 'excursao/atualizar_excursao.html', {'form': form, 'excursion' : excursion})


@login_required
def deletar_excursao(request, pk):
    excursion = get_object_or_404(Excursion, pk=pk)
    if excursion.delete():
        return redirect('../listar')
    else:
        return server_errror(request, 'ops_500.html')
    return render(request, '/../listar.html', {'excursion': excursion})


@login_required
def adicionar_excursao(request):
    form = None
    if request.method == 'POST':
        form = ExcursionForm(request.POST)
        if form.is_valid():
            excursion                   = form.save(commit=False)
            excursion.registration_user = request.user
            excursion.travel_agency     = get_agency_user(request.user)
            excursion.activate          = True    
            excursion.save()
            form.save_m2m()
            messages.success(request, 'Excursão cadastrada com sucesso!')
            return redirect('listar_excursao')
    else:
        form = ExcursionForm()
    return render(
        request,
        'excursao/adicionar_excursao.html',
        {'form': form},
    )


@login_required
def adicionar_destino(request):
    form = None
    if request.method == 'POST':
        form = DestinyForm(request.POST)
        if form.is_valid():
            destiny                 = form.save(commit=False)
            destiny.travel_agency   = get_agency_user(request.user)
            destiny.activate        = True
            destiny.save()
            messages.success(request, 'Destino mapeado com sucesso!')
            return redirect('listar_destino')
    else:
        form = DestinyForm()
    return render(
        request,
        'excursao/adicionar_destino.html',
        {'form': form},
    )


@login_required
def listar_destino(request):
    destinations = Destiny.objects.filter(travel_agency=get_agency_user(request.user).pk)
    return render(request, 'excursao/listar_destino.html', {'destinations': destinations})


@login_required
def atualizar_destino(request, pk):
    destiny = get_object_or_404(Destiny, pk=pk)
    form = DestinyForm(instance=destiny)
    if request.method == 'POST':
        form = DestinyForm(request.POST, instance=destiny)    
        if form.is_valid():
            destiny                 = form.save(commit=False)
            destiny.name            = form.cleaned_data['name']
            destiny.country         = form.cleaned_data['country']
            destiny.state           = form.cleaned_data['state']
            destiny.city            = form.cleaned_data['city']
            destiny.neighborhood    = form.cleaned_data['neighborhood']
            destiny.zip_code        = form.cleaned_data['zip_code']
            destiny.save()
            messages.success(request, 'Destino atualizado!')
            return redirect('listar_destino')
        else:
            return render(request, 'excursao/atualizar_destino.html', {'form': form, 'destiny': destiny})
    
    elif request.method == 'GET':
        return render(request, 'excursao/atualizar_destino.html', {'form': form, 'destiny': destiny})


@login_required
def deletar_destino(request, pk):
    destiny = get_object_or_404(Destiny, pk=pk)
    if destiny.delete():
        return redirect('listar_destino')
    else:
        return server_errror(request, 'ops_500.html')


def get_agency_user(user_id):
    profile         = Profile.objects.get(user_id=user_id)
    travel_agency   = TravelAgency.objects.get(profile=profile)
    return travel_agency


@login_required
def adicionar_transporte(request):
    form = TransportForm()
    if request.method == 'POST':
        form = TransportForm(request.POST)
        if form.is_valid():
            transport               = form.save(commit=False)
            transport.activate      = True
            transport.travel_agency = get_agency_user(request.user)
            messages.success(request, 'Transporte cadastrado com sucesso!')
            return redirect('adicionar_orcamento')
        else:
            messages.error(request, 'Formulário contém erros!!!')    
    
    return render(request, 'excursao/adicionar_transporte.html', {'form': form})


@login_required
def atualizar_transporte(request, pk):
    transport = get_object_or_404(Transport, pk=pk)
    form = TransportForm(instance=transport)
    if request.method == 'POST':
        form = TransportForm(request.POST, instance=transport)    
        if form.is_valid():
            transport                   = form.save(commit=False)
            transport.service_provider  = form.cleaned_data['service_provider']
            transport.model             = form.cleaned_data['model']
            transport.brand             = form.cleaned_data['brand']
            transport.year              = form.cleaned_data['ano']
            transport.seats             = form.cleaned_data['seats']
            transport.bathroom          = form.cleaned_data['bathroom']
            transport.minibar           = form.cleaned_data['minibar']
            transport.air_conditioning  = form.cleaned_data['air_conditioning']
            transport.sound             = form.cleaned_data['sound']
            transport.tv                = form.cleaned_data['tv']
            transport.details           = form.cleaned_data['details']                        
            transport.save()
            messages.success(request, 'Sucesso')
            return redirect('listar_transporte')
        else:
            return render(request, 'excursao/atualizar_transporte.html', {'form': form, 'transport': transport})
    
    elif request.method == 'GET':
        return render(request, 'excursao/atualizar_transporte.html', {'form': form, 'transport': transport})



@login_required
def listar_transporte(request):
    transport_list = Transport.objects.filter(travel_agency=get_agency_user(request.user).pk)
    return render(request, 'excursao/listar_transporte.html', {'transport_list': transport_list})


@login_required
def deletar_transporte(request, pk):
    transport = get_object_or_404(Transport, pk=pk)
    if transport.delete():
        return redirect('listar_transporte')
    else:
        return server_errror(request, 'ops_500.html')


@login_required
def adicionar_prestador_servico(request):
    form = None
    if request.method == 'POST':
        form = ServiceProviderForm(request.POST)
        if form.is_valid():
            service_provider                = form.save(commit=False)
            service_provider.acitvate       = True
            service_provider.travel_agency  = get_agency_user(request.user)
            service_provider.save()
            messages.success(request, 'Prestador de Serviço cadastrado com sucesso!')
            return redirect('listar_prestador_servico')
    else:
        form = ServiceProviderForm()
    return render(request, 'excursao/adicionar_prestador_servico.html', {'form': form})


@login_required
def atualizar_prestador_servico(request, pk):
    service_provider    = get_object_or_404(ServiceProvider, pk=pk)
    form = ServiceProviderForm(instance=service_provider)
    if request.method == 'POST':
        form = ServiceProviderForm(request.POST, instance=service_provider)
        if form.is_valid():
            service_provider                = form.save(commit=False)
            service_provider.name           = form.cleaned_data['name']
            service_provider.cnpj_cpf       = form.cleaned_data['cnpj_cpf']
            service_provider.legal_person   = form.cleaned_data['legal_person']
            service_provider.cadastur       = form.cleaned_data['cadastur']
            service_provider.email          = form.cleaned_data['email']
            service_provider.cell_phone     = form.cleaned_data['cell_phone']
            service_provider.adress         = form.cleaned_data['adress']
            service_provider.business_hours = form.cleaned_data['business_hours']
            service_provider.save()
            messages.success(request, 'Prestador de Serviço atualizado!')
            return redirect('listar_prestador_servico')
        else:
            return render(request, 'excursao/atualizar_prestador_servico.html', {'form': form, 'service_provider': service_provider})

    elif request.method == 'GET':
        return render(request, 'excursao/atualizar_prestador_servico.html', {'form': form, 'service_provider': service_provider})


@login_required
def listar_prestador_servico(request):
    service_providers = ServiceProvider.objects.filter(travel_agency=get_agency_user(request.user).pk)
    return render(request, 'excursao/listar_prestador_servico.html', {'service_providers': service_providers})
 

def get_service_provider_type(request, pk):
    service_providers       = ServiceProvider.objects.filter(travel_agency=get_agency_user(request.user).pk, service_provider_type=pk)
    service_providers_dict  = {}
    for service_provider in service_providers:
        service_providers_dict[service_provider.id] = service_providers.name
    return HttpResponse(json.dumps(service_providers_dict), content_type="application/json")


@login_required
def deletar_prestador_servico(request, pk):
    service_provider = get_object_or_404(ServiceProvider, pk=pk)
    if service_provider.delete():
        return redirect('listar_prestador_servico')
    else:
        return server_errror(request, 'ops_500.html')

@login_required
def adicionar_orcamento(request):
    form = EstimateForm()
    if request.method == 'POST':
        form = EstimateForm(request.POST)
        if form.is_valid():
            estimate = form.save(commit=False)
            if Estimate.objects.filter(nome=estimate.name).exists():
                messages.error(request, 'Já existe um orçamento com este nome.')
            else:
                estiamte.travel_agency  = get_agency_user(request.user)
                estimate.activate       = True
                estimate.save()
                messages.success(request, 'Orçamento cadastrado com sucesso!')
                return redirect('listar_orcamento')
        else:
            messages.error(request, 'Formulário contém erros!!!')     
    return render(request, 'excursao/adicionar_orcamento.html', {'form': form})


@login_required
def atualizar_orcamento(request, pk):
    estimate = get_object_or_404(Estimate, pk=pk)
    form = EstimateForm(instance=estimate)
    if request.method == 'POST':
        form = EstimateForm(request.POST, instance=estimate)
        if form.is_valid():
            estimate                        = form.save(commit=False)
            estimate.excursion              = form.cleaned_data['excursion']
            estimate.service_provider_type  = form.cleaned_data['service_provider_type']
            estimate.service_provider       = form.cleaned_data['service_provider']
            estimate.cost                   = form.cleaned_data['cost']
            estimate.start_time             = form.cleaned_data['start_time']
            estimate.end_time               = form.cleaned_data['end_time']
            estimate.selected               = form.cleaned_data['selected']
            estimate.details                = form.cleaned_data['details']
            estimate.save()
            messages.success(request, 'Orçamento atualizado!')
            return redirect('listar_orcamento')
        else:
            return render(request, 'excursao/atualizar_orcamento.html', {'form': form, 'estimate': estimate})

    elif request.method == 'GET':
        return render(request, 'excursao/atualizar_orcamento.html', {'form': form, 'estimate': estimate})
                                 

@login_required
def listar_orcamento(request):
    estimates = Estimate.objects.filter(travel_agency=get_agency_user(request.user).pk)
    return render(request, 'excursao/listar_orcamento.html', {'estiamtes': estimates})


@login_required
def deletar_orcamento(request, pk):
    estimate = get_object_or_404(Estimate, pk=pk)
    if estimate.delete():
        return redirect('listar_orcamento')
    else:
        return server_errror(request, 'ops_500.html')


@login_required
def adicionar_roteiro(request):
    form = TravelItineraryForm()
    if request.method == 'POST':
        form = TravelItineraryForm(request.POST)
        if form.is_valid():
            travel_itinerary = form.save(commit=False)
            travel_itinerary.activate = True
            travel_itinerary.travel_agency = get_agency_user(request.user)
            travel_itinerary.save()
            messages.success(request, 'Roteiro cadastrado com sucesso!')
            return redirect('listar_roteiro')
        else:
            messages.error(request, 'Formulário contém erros!')     
    return render(request, 'excursao/adicionar_roteiro.html', {'form': form})


@login_required
def atualizar_roteiro(request, pk):
    travel_itinerary = get_object_or_404(TravelItinerary, pk=pk)
    form = TravelItineraryForm(instance=travel_itinerary)
    if request.method == 'POST':
        form = TravelItineraryForm(request.POST, instance=travel_itinerary)
        if form.is_valid():
            travel_itinerary            = form.save(commit=False)
            travel_itinerary.excursion  = form.cleaned_data['excursion']
            travel_itinerary.start_time = form.cleaned_data['start_time']
            travel_itinerary.end_time   = form.cleaned_data['end_time']
            travel_itinerary.paid       = form.cleaned_data['paid']
            travel_itinerary.inclusive  = form.cleaned_data['inclusive']
            travel_itinerary.cost       = form.cleaned_data['cost']
            travel_itinerary.details    = form.cleaned_data['details']
            travel_itinerary.save()
            messages.success(request, 'Roteiro atualizado!')
            return redirect('listar_roteiro')
        else:
            return render(request, 'excursao/atualizar_roteiro.html', {'form': form, 'travel_itinerary': travel_itinerary})

    elif request.method == 'GET':
        return render(request, 'excursao/atualizar_roteiro.html', {'form': form, 'travel_itinerary': travel_itinerary})
                                 

@login_required
def listar_roteiro(request):
    travel_intineraries = TravelItinerary.objects.filter(travel_agency=get_agency_user(request.user).pk)
    return render(request, 'excursao/listar_roteiro.html', {'travel_intineraries': travel_intineraries})


@login_required
def deletar_roteiro(request, pk):
    travel_intinerary = get_object_or_404(TravelItinerary, pk=pk)
    if travel_intinerary.delete():
        return redirect('listar_roteiro')
    else:
        return server_errror(request, 'ops_500.html')