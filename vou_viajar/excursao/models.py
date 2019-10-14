"""
Models da aplicação 'excursao'.
"""

from django.contrib.auth.models import User
from django.db import models
from vou_viajar.conta.models import Agencia
# Create your models here.

class Destino(models.Model):
    
    nome_turistico = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    agencia = models.ForeignKey(Agencia, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nome_turistico

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
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    horario_inicio = models.DateTimeField()
    horario_fim = models.DateTimeField()
    origem = models.CharField(max_length=20, null=False)
    destino = models.ManyToManyField(Destino)
    usuario_cadastro = models.ForeignKey(User, on_delete=models.PROTECT)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    agencia = models.ForeignKey(Agencia, on_delete=models.PROTECT)

    def __str__(self):
        return '%s %s' % (self.titulo, self.nome_turistico)


class PrestadorServico(models.Model):
    agencia = models.ForeignKey(Agencia, on_delete=models.PROTECT)    
    cnpj_cpf = models.CharField(max_length=50)
    pessoa_juridica = models.BooleanField(null=True, blank=False)
    cadastur = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=False)
    telefone = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    horario_funcionamento = models.CharField(max_length=50)


class Transporte(models.Model):
    agencia = models.ForeignKey(Agencia, on_delete=models.PROTECT)
    prestador_servico = models.ForeignKey(PrestadorServico, on_delete=models.PROTECT)
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)    
    ano = models.IntegerField(null=True, blank=False)
    poltronas = models.IntegerField(null=True, blank=False)
    banheiro = models.BooleanField(null=True, blank=False)
    frigobar = models.BooleanField(null=True, blank=False)
    ar_condicionado = models.BooleanField(null=True, blank=False)
    som = models.BooleanField(null=True, blank=False)
    tv = models.BooleanField(null=True, blank=False)

class Orcamento(models.Model):
    pass

class Roteiro(models.Model):
    pass
