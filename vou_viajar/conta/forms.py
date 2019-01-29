from django import forms

from .models import Agencia

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
            'site_oficial',
        ]

