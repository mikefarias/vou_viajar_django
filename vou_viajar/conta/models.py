"""
Models da aplicação 'conta'.
"""

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Agencia(models.Model):
    """
    A class Agencia representa uma agência turística.
    """

    cod_cadastur = models.CharField(max_length=10, null=False, blank=False)
    cnpj_cpf = models.CharField(max_length=14, null=False, blank=False)
    nome_juridico = models.CharField(max_length=100, null=False, blank=False)
    nome_fantasia = models.CharField(max_length=100, null=False, blank=False)
    nome_responsavel = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    cpf_responsavel = models.CharField(max_length=14)
    agencia_fisica = models.BooleanField(null=False, blank=False)
    foto_perfil = models.ImageField(null=True, blank=True)
    endereco = models.CharField(max_length=200)
    email = models.EmailField(null=False, blank=False)
    telefone = models.CharField(max_length=11)
    fan_page_oficial = models.URLField(null=True, blank=True)
    instagram_oficial = models.URLField(null=True, blank=True)
    site_oficial = models.URLField(null=True, blank=True)
    usuario_cadastro = models.ForeignKey(User, on_delete=models.PROTECT)
    data_cadastro = models.DateTimeField(auto_now_add=True)
