"""
Models da aplicação 'excursao'.
"""

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Excursao(models.Model):
    """
    A class Excursao representa uma excursão turística.
    """

    SITUACAO_ATIVO = 1
    SITUACAO_REALIZADA = 2
    SITUACAO_CANCELADO = 3
    SITUACAO_EXCLUIDO = 0
    SITUACOES_CHOICES = (
        (SITUACAO_EXCLUIDO, 'Excluído'),
        (SITUACAO_ATIVO, 'Ativo'),
        (SITUACAO_REALIZADA, 'Realizada'),
        (SITUACAO_CANCELADO, 'Cancelado'),
    )

    TIPO_EXCURSAO = 1
    TIPO_BATEVOLTA = 2
    TIPOS_CHOICES = (
        (TIPO_EXCURSAO, 'Excursão'),
        (TIPO_BATEVOLTA, 'Bate volta'),
    )

    tipo = models.IntegerField(
        default=TIPO_EXCURSAO,
        choices=TIPOS_CHOICES,
    )
    situacao = models.IntegerField(
        default=SITUACAO_ATIVO,
        choices=SITUACAO_EXCLUIDO,
    )
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(default='')
    horario_inicio = models.DateTimeField()
    horario_fim = models.DateTimeField()
    origem = models.CharField(max_length=100, null=False)
    destino = models.CharField(max_length=100, null=False)
    usuario_cadastro = models.ForeignKey(User, on_delete=models.PROTECT)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo



class Destino(models.Model):

    nome_turistico = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    
    def __str__(self):
        return self.titulo