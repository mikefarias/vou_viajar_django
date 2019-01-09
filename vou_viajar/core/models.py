from django.db import models
from model_utils import Choices


class Evento(models.Model):

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



