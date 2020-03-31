from django.contrib.auth.forms import AuthenticationForm

from django import forms
from .models import Agencia
from .models import Pessoa
from .models import User


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id': 'id_username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={ 'class': 'form-control', 'placeholder': '', 'id': 'id_password'}))


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
            'endereco'
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