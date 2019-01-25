from django import forms

from .models import Excursao
from .models import Agencia


class ExcursaoForm(forms.ModelForm):
    horario_inicio = forms.SplitDateTimeField(
        widget=forms.SplitDateTimeWidget(date_attrs={'type': 'date'}, time_attrs={'type': 'time'}))
    horario_fim = forms.SplitDateTimeField(
        widget=forms.SplitDateTimeWidget(date_attrs={'type': 'date'}, time_attrs={'type': 'time'}))

    class Meta:
        model = Excursao
        fields = [
            'titulo',
            'descricao',
            'origem',
            'destino',
            'horario_inicio',
            'horario_fim'
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
