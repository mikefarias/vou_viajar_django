from django import forms
from .models import Agencia
from .models import Pessoa

class AgenciaForm(forms.ModelForm):

    nome_fantasia = forms.CharField(label='Nome da Agência')
    nome_juridico = forms.CharField(label='Razão Social', help_text='Informe o nome associado ao CNPJ')
    cnpj = forms.CharField(label='CNPJ')
    cod_cadastur = forms.CharField(label='Nº Cadastur')
    class Meta:
        model = Agencia
        fields = [
            'nome_juridico',
            'nome_fantasia',
            'cod_cadastur',
            'cnpj',
            'agencia_fisica',
            'foto_perfil',

        ]

class PessoaForm(forms.ModelForm):

    nome = forms.CharField(label='Nome', help_text='Informe seu nome completo')
    cpf = forms.CharField(label='CPF')
    class Meta:
        model = Pessoa
        fields = [
            'nome',
            'cpf',
        ]