from django import forms

from .models import Excursao
from .models import Destino
from .models import PrestadorServico


class ExcursaoForm(forms.ModelForm):

    titulo = forms.CharField(label='Título', help_text='Em até 50 caracteres')
    descricao = forms.CharField(label='Descrição',  help_text='Em até 100 caracteres')
    destino = forms.ModelMultipleChoiceField(
        queryset=Destino.objects.all()),
    horario_inicio = forms.SplitDateTimeField(
        widget=forms.SplitDateTimeWidget(
            date_attrs={'type': 'date'},
            time_attrs={'type': 'time'},
        )
    )
    horario_fim = forms.SplitDateTimeField(
        widget=forms.SplitDateTimeWidget(
            date_attrs={'type': 'date'},
            time_attrs={'type': 'time'},
        )
    )

    class Meta:
        model = Excursao
        fields = [
            'titulo',
            'descricao',
            'origem',
            'destino',
            'horario_inicio',
            'horario_fim',
        ]


class DestinoForm(forms.ModelForm):
    
    class Meta:
        model = Destino
        fields = [
            'nome_turistico',
            'pais',
            'estado',
            'cidade',
            'bairro',
            'cep',
        ]


class PrestadorForm(forms.ModelForm):

    cnpj_cpf = forms.CharField(label='CPNJ/CPF')
    pessoa_juridica = forms.BooleanField(label='Pessoa Jurídica')
    cadastur = forms.CharField(label='Cadastur')
    email = forms.EmailField(label='E-mail')
    telefone = forms.CharField(label='Telefone')
    endereco = forms.CharField(label='Endereço')
    horario_funcionamento = forms.CharField(label='Horário de Funcionamento')

    class Meta: 
        model = PrestadorServico
        fields = [
            'cnpj_cpf',
            'pessoa_juridica',
            'cadastur',
            'email',
            'telefone',
            'endereco',
            'horario_funcionamento',
        ]



