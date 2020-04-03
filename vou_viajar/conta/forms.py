from django.contrib.auth.forms import AuthenticationForm

from django import forms
from .models import TravelAgency, User



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


class ContactTravelAgencyForm(forms.ModelForm):
    
    email           = forms.EmailField(label='Email')
    phone_number    = forms.CharField(label='Contato telefônico')
    whatsapp        = forms.CharField(label='Contato Whatsapp')
    fan_pag         = forms.URLField(label='Perfil Facebook')
    instagram       = forms.URLField(label='Perfil Instagram')
    website         = forms.URLField(label='Site Institucional')


class TravelAgencyForm(forms.ModelForm):

    code_cadastur   = forms.CharField(label='Nº Cadastur')
    cnpj            = forms.IntegerField(label='CNPJ da Agência')    
    physical_agency = forms.BooleanField(label='Agência Física?')
    address         = forms.CharField(label='Endereço')
    logo            = forms.ImageField(label='Logo da Agência')

    class Meta:
        model = TravelAgency
        fields = [
            'code_cadastur',
            'cnpj',
            'physical_agency',
            'address',
            'logo'
        ]    


class ProfileForm(forms.ModelForm):

    cpf_cnpj        = forms.CharField(label='CNPJ ou CPF')
    profile_photo   = forms.ImageField(label='Foto de Perfil')
    phone_number    = forms.CharField(label='Nº contato')
    whatsapp        = forms.CharField(label='Whatsapp')
