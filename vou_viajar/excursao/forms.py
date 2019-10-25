from django import forms

from .models import Excursao, Transporte
from .models import Destino
from .models import PrestadorServico
from .models import TipoPrestadorServico


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

    categoria = forms.ModelMultipleChoiceField(queryset=TipoPrestadorServico.objects.all()),
    nome = forms.CharField(label='Nome do Prestador de Serviço')
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
            'categoria',
            'nome',
            'cnpj_cpf',
            'pessoa_juridica',
            'cadastur',
            'email',
            'telefone',
            'endereco',
            'horario_funcionamento',
        ]

class TransporteForm(forms.ModelForm):

    prestador_servico = forms.ModelChoiceField(queryset=PrestadorServico.objects.all(), label='Prestador de Serviço')
    modelo = forms.CharField(label='Modelo do Transporte')
    marca = forms.CharField(label='Marca')
    ano = forms.IntegerField(label='Ano')
    poltronas = forms.IntegerField(label='Quantidade de Poltronas')
    banheiro = forms.BooleanField(label='Tem banheiro?')
    frigobar = forms.BooleanField(label='Tem frigobar?')
    ar_condicionado = forms.BooleanField(label='Tem ar-condicionado?')
    som = forms.BooleanField(label='Tem som?')
    tv = forms.BooleanField(label='Tem TV?')
    observacao = forms.CharField(label='Observações sobre o veículo')

    class Meta:
        model = Transporte
        fields = [
            'prestador_servico',
            'modelo',
            'marca',
            'ano',
            'poltronas',
            'banheiro',
            'frigobar',
            'ar_condicionado',
            'som',
            'tv',
            'observacao',
        ]



