from django import forms

from core.models import Evento
from core.models import Agencia


class EventoForm(forms.ModelForm):
    inicio_evento = forms.SplitDateTimeField(
        widget=forms.SplitDateTimeWidget(date_attrs={'type': 'date'}, time_attrs={'type': 'time'}))
    fim_evento = forms.SplitDateTimeField(
        widget=forms.SplitDateTimeWidget(date_attrs={'type': 'date'}, time_attrs={'type': 'time'}))

    class Meta:
        model = Evento
        fields = [
            'titulo',
            'descricao',
            'origem',
            'destino',
            'inicio_evento',
            'fim_evento'
        ]


class AgenciaForm(forms.ModelForm):

    class Meta:
        model = Agencia
        fields = [
        'cnpj_cpf',
        'nome_juridico',
        'nome_fantasia',
        'cod_cadastur',
        'nome_responsavel',
        'cpf_responsavel',
        'agencia_fisica',
        'foto_perfil',
        'endereco',
        'email',
        'telefone',
        'fan_page_oficial',
        'instagram_oficial',
        'site_oficial'
        ]
