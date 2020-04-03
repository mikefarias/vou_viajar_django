"""
Models da aplicação 'excursao'.
"""

from django.contrib.auth.models import User
from django.db import models
from vou_viajar.conta.models import TravelAgency
from django.conf import settings


class Destino(models.Model):
    
    nome_turistico = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    agencia = models.ForeignKey(TravelAgency, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nome_turistico


class TipoExcusao(models.Model):
    descricao = models.CharField(max_length=100)
    codigo = models.PositiveIntegerField()
    ativo = models.NullBooleanField()

class SituacaoExcusao(models.Model):
    descricao = models.CharField(max_length=100)
    codigo = models.PositiveIntegerField()
    ativo = models.NullBooleanField()

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

    tipo = models.IntegerField(default=1)
    situacao = models.IntegerField(default=1)
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    horario_inicio = models.DateTimeField()
    horario_fim = models.DateTimeField()
    origem = models.CharField(max_length=20, null=False)
    destino = models.ManyToManyField(Destino)
    usuario_cadastro = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    agencia = models.ForeignKey(TravelAgency, on_delete=models.PROTECT)

    def __str__(self):
        return '%s' % (self.titulo)


class TipoPrestadorServico(models.Model):
    descricao = models.CharField(max_length=20)

    def __str__(self):
        return '%s' % (self.descricao)


class PrestadorServico(models.Model):
    agencia = models.ForeignKey(TravelAgency, on_delete=models.PROTECT)
    categoria = models.ForeignKey(TipoPrestadorServico, on_delete=models.PROTECT)
    nome = models.CharField(max_length=50)
    cnpj_cpf = models.CharField(max_length=50)
    pessoa_juridica = models.BooleanField(null=True, blank=False)
    cadastur = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=False)
    telefone = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    horario_funcionamento = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.nome)

class TipoServico(models.Model):
    descricao = models.CharField(max_length=20)

    def __str__(self):
        return '%s' % (self.descricao)


class Transporte(models.Model):
    agencia = models.ForeignKey(TravelAgency, on_delete=models.PROTECT)
    prestador_servico = models.ForeignKey(PrestadorServico, on_delete=models.PROTECT)
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)    
    ano = models.IntegerField(null=True, blank=False)
    poltronas = models.IntegerField(null=True, blank=False)
    banheiro = models.BooleanField(default=False, null=True, blank=True)
    frigobar = models.BooleanField(default=False, null=True, blank=True)
    ar_condicionado = models.BooleanField(default=False, null=True, blank=True)
    som = models.BooleanField(default=False, null=True, blank=True)
    tv = models.BooleanField(default=False, null=True, blank=True)
    observacao = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % (self.modelo)


class Orcamento(models.Model):
    agencia = models.ForeignKey(TravelAgency, on_delete=models.PROTECT)
    excursao = models.ForeignKey(Excursao, on_delete=models.PROTECT)
    tipo_prestador_servico = models.ForeignKey(TipoPrestadorServico, on_delete=models.PROTECT)
    prestador_servico = models.ForeignKey(PrestadorServico, on_delete=models.PROTECT)
    cotacao = models.IntegerField(null=False)
    horario_partida = models.DateTimeField()
    horario_chegada = models.DateTimeField()
    selecionado = models.BooleanField(default=False, null=True, blank=True)
    observacao = models.CharField(max_length=100)


class OrcamentoDetalhesTransporte(models.Model):
    orcamento = models.ForeignKey(Orcamento, on_delete=models.PROTECT)
    transporte = models.ForeignKey(Transporte, on_delete=models.PROTECT)


class Roteiro(models.Model):
    agencia = models.ForeignKey(TravelAgency, on_delete=models.PROTECT)
    excursao = models.ForeignKey(Excursao, on_delete=models.PROTECT)
    horario_inicio = models.DateTimeField()
    horario_fim = models.DateTimeField()
    pago = models.BooleanField(default=False, null=True, blank=True)
    incluso = models.BooleanField(default=False, null=True, blank=True)
    custo = models.IntegerField(null=False)
    observacao = models.CharField(max_length=100)