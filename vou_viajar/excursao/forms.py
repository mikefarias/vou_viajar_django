from django import forms

from .models import Excursion, Destiny, Transport, ServiceProvider, ServiceProviderType, Estimate, TravelItinerary


class ExcursionForm(forms.ModelForm):

    name        = forms.CharField(label='Nome da Excursão', help_text='Em até 50 caracteres')
    details     = forms.CharField(label='Detalhes da Excursão',  help_text='Em até 100 caracteres')
    origin      = forms.CharField(label='Partida')
    destiny     = forms.ModelMultipleChoiceField(queryset=Destiny.objects.all())
    start_time  = forms.SplitDateTimeField( widget=forms.SplitDateTimeWidget(
                                                date_attrs={'type': 'date'},
                                                time_attrs={'type': 'time'},)
                                        )
    end_time    = forms.SplitDateTimeField( widget=forms.SplitDateTimeWidget(
                                                date_attrs={'type': 'date'},
                                                time_attrs={'type': 'time'},)
                                        )

    class Meta:
        model = Excursion
        fields = [
            'name',
            'details',
            'excursion_situation',
            'excursion_type',
            'origin',
            'destiny',
            'start_time',
            'end_time',
        ]


class DestinyForm(forms.ModelForm):
    
    class Meta:
        model = Destiny
        fields = [
            'name',
            'country',
            'state',
            'city',
            'neighborhood',
            'zip_code',
        ]

class ServiceProviderForm(forms.ModelForm):

    service_provider_type   = forms.ModelMultipleChoiceField(queryset=ServiceProviderType.objects.all()),
    name                    = forms.CharField(label='Nome do Prestador de Serviço')
    cnpj_cpf                = forms.CharField(label='CPNJ/CPF')
    legal_person            = forms.BooleanField(label='Pessoa Jurídica')
    cadastur                = forms.CharField(label='Cadastur')
    email                   = forms.EmailField(label='E-mail')
    cell_phone              = forms.CharField(label='Telefone')
    adress                  = forms.CharField(label='Endereço')
    business_hours          = forms.CharField(label='Horário de Funcionamento')

    class Meta: 
        model = ServiceProvider
        fields = [
            'service_provider_type',
            'name',
            'cnpj_cpf',
            'legal_person',
            'cadastur',
            'email',
            'cell_phone',
            'adress',
            'business_hours',
        ]

class TransportForm(forms.ModelForm):

    service_provider    = forms.ModelChoiceField(queryset=ServiceProvider.objects.all(), label='Prestador de Serviço')
    model               = forms.CharField(label='Modelo do Transporte')
    brand               = forms.CharField(label='Marca')
    years               = forms.IntegerField(label='Ano')
    seats               = forms.IntegerField(label='Quantidade de Poltronas')
    bathroom            = forms.BooleanField(label='Tem banheiro?', required=False)
    minibar             = forms.BooleanField(label='Tem frigobar?', required=False)
    air_conditioning    = forms.BooleanField(label='Tem ar-condicionado?', required=False)
    sound               = forms.BooleanField(label='Tem som?', required=False)
    tv                  = forms.BooleanField(label='Tem TV?', required=False)
    details             = forms.CharField(label='Observações sobre o veículo')

    class Meta:
        model = Transport
        fields = [
            'service_provider',
            'model',
            'brand',
            'year',
            'seats',
            'bathroom',
            'minibar',
            'air_conditioning',
            'sound',
            'tv',
            'details',
        ]


class EstimateForm(forms.ModelForm):
    name                    = forms.CharField(label='Nome do orçamento')
    excursion               = forms.ModelChoiceField(queryset=Excursion.objects.all(), label='Excursão')
    service_provider_type   = forms.ModelChoiceField(queryset=ServiceProviderType.objects.all(), label='Categoria Prestação de Serviço')
    service_provider        = forms.ModelChoiceField(queryset=ServiceProvider.objects.all(), label='Prestador de Serviço')
    cost                    = forms.IntegerField(label='Custo')
    start_time              = forms.SplitDateTimeField( widget=forms.SplitDateTimeWidget(
                                                                date_attrs={'type': 'date'},
                                                                time_attrs={'type': 'time'},
                                                            ),
                                                            label='Horário Partida',
                                                            help_text='Data e hora que o transporte ficará disponível para agência'
                                                        )
    end_time                = forms.SplitDateTimeField( widget=forms.SplitDateTimeWidget(
                                            date_attrs={'type': 'date'},
                                            time_attrs={'type': 'time'},
                                        ),
                                        label='Horário Chegada',
                                        help_text='Data e hora que o transporte deverá ser devolvido'
    )
    selected                = forms.BooleanField(label='Selecionado', required=False)
    details                 = forms.CharField()

    class Meta:
        model = Estimate
        fields = [
            'name',
            'excursion',
            'service_provider_type', 
            'service_provider',
            'cost',
            'start_time',
            'end_time',
            'selected',
            'details'
        ]

class TravelItineraryForm(forms.ModelForm):
    excursion   = forms.ModelChoiceField(queryset=Excursion.objects.all(), label = 'Excursão')
    start_time  = forms.SplitDateTimeField( widget=forms.SplitDateTimeWidget(
                                            date_attrs={'type': 'date'},
                                            time_attrs={'type': 'time'},
                                        ),
                                        label='Horário Início',
                                        help_text='Horário de início da atividade'
                                    )
    end_time    = forms.SplitDateTimeField(
        widget=forms.SplitDateTimeWidget(
            date_attrs={'type': 'date'},
            time_attrs={'type': 'time'},
        ),
        label='Horário Fim',
        help_text='Horário do fim da atividade'
    )
    paid        = forms.BooleanField(label='Pago', required=False)
    inclusive   = forms.BooleanField(label='Incluso', required=False)
    cost        = forms.IntegerField(label='Custo')
    details     = forms.CharField(label='Detalhes')

    class Meta: 
        model  = TravelItinerary
        fields = [
            'excursion',
            'start_time',
            'end_time',
            'paid',
            'inclusive',
            'cost',
            'details'
        ]