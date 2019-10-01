"""
Models da aplicação 'conta'.
"""

from django.contrib.auth.models import User
from django.db import models

from django.utils import timezone
import datetime

# Create your models here.

class Agencia(models.Model):
    """
    A class Agencia representa uma agência turística.
    """

    nome_juridico = models.CharField(max_length=100, null=False, blank=False)
    nome_fantasia = models.CharField(max_length=100, null=False, blank=False)
    cod_cadastur = models.CharField(max_length=10, null=False, blank=False)
    cnpj = models.CharField(max_length=14, null=False, blank=False)
    agencia_fisica = models.BooleanField(null=False, blank=False)
    foto_perfil = models.ImageField(null=True, blank=True)
    endereco = models.CharField(max_length=200)
    usuario_cadastro = models.ForeignKey(User, on_delete=models.PROTECT)
    data_cadastro = models.DateTimeField(auto_now_add=True)


class ContatoAgencia(models.Model):

    email = models.EmailField(null=False, blank=False)
    contato = models.CharField(max_length=11)
    fan_page_oficial = models.URLField(null=True, blank=True)
    instagram_oficial = models.URLField(null=True, blank=True)
    site_oficial = models.URLField(null=True, blank=True)

class Pessoa(models.Model):

    nome = models.CharField(
        max_length=100,
        null=False,
        blank=False, )
    cpf = models.CharField(max_length=14)
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    agencia = models.ForeignKey(Agencia, on_delete=models.PROTECT)



class ContatoPessoa(models.Model):

    email = models.EmailField(null=False, blank=False)
    contato = models.CharField(max_length=11)
    whatsapp = models.CharField(max_length=11)