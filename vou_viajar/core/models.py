from django.db import models
from model_utils import Choices


class Excursao(models.Model):

    SITUACOES = Choices(
        (1, 'ATIVO', 'Ativo'),
        (2, 'EXPIRADO', 'Expirado'),
        (3, 'CANCELADO', 'Cancelado')
    )

    TIPO = Choices(
        (1, 'EXCURSAO', 'Excursao'),
        (2, 'BATE_VOLTA', 'Bate Volta'),
        (3, 'CANCELADO', 'Cancelado')
    )

    titulo = models.CharField(max_length=100)
    descricao = models.TextField(default='')
    inicio_evento = models.DateTimeField()
    fim_evento = models.DateTimeField()

    origem = models.CharField(max_length=100, null=False)
    destino = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.titulo


class Agencia(models.Model):

    cnpj_cpf = models.CharField(max_length=14, null=False, blank=False)
    nome_juridico = models.TextField(max_length=30, null=False, blank=False)
    nome_fantasia = models.TextField(max_length=30, null=False, blank=False)
    cod_cadastur = models.CharField(max_length=10, null=False, blank=False) #quantos digitos ??
    nome_responsavel = models.TextField(max_length=30, null=False, blank=False)
    cpf_responsavel = models.TextField(max_length=14)
    agencia_fisica = models.BooleanField(null=False, blank=False)
    foto_perfil = models.ImageField(null=True, blank=True)
    endereco = models.TextField(max_length=30)
    email = models.EmailField(null=False, blank=False)
    telefone = models.CharField(max_length=11)
    fan_page_oficial = models.URLField(null=True, blank=True)
    instagram_oficial = models.URLField(null=True, blank=True)
    site_oficial = models.URLField(null=True, blank=True)






