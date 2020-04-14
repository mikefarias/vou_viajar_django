"""
Models da aplicação 'excursao'.
"""

from django.contrib.auth.models import User
from django.db import models
from vou_viajar.conta.models import TravelAgency
from django.conf import settings


class Destiny(models.Model):    
    name                = models.CharField(max_length=100)
    country             = models.CharField(max_length=100)
    state               = models.CharField(max_length=100)
    city                = models.CharField(max_length=100)
    neighborhood        = models.CharField(max_length=100)
    zip_code            = models.CharField(max_length=100)
    created_on          = models.DateTimeField(auto_now_add=True)
    modified_on         = models.DateTimeField(auto_now_add=True)
    active              = models.BooleanField(default=True)
    registration_user   = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    travel_agency       = models.ForeignKey(TravelAgency, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class ExcursionType(models.Model):
    name    = models.CharField(max_length=100)
    code    = models.PositiveIntegerField()
    active  = models.NullBooleanField()


class ExcursionSituation(models.Model):
    name    = models.CharField(max_length=100)
    code    = models.PositiveIntegerField()
    active  = models.NullBooleanField()


class Excursion(models.Model):
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

    excursion_type      = models.OneToOneField(ExcursionType, on_delete=models.CASCADE)
    excursion_situation = models.OneToOneField(ExcursionSituation, on_delete=models.CASCADE)
    name                = models.CharField(max_length=50)
    details             = models.CharField(max_length=100)
    start_time          = models.DateTimeField()
    end_time            = models.DateTimeField()
    origin              = models.CharField(max_length=20, null=False)
    destiny             = models.ManyToManyField(Destiny)
    created_on          = models.DateTimeField(auto_now_add=True)
    modified_on         = models.DateTimeField(auto_now_add=True)
    active              = models.BooleanField(default=True)
    registration_user   = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    travel_agency       = models.ForeignKey(TravelAgency, on_delete=models.PROTECT)

    def __str__(self):
        return '%s' % (self.name)


class ServiceProviderType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return '%s' % (self.name)


class ServiceProvider(models.Model):
    service_provider_type   = models.ForeignKey(ServiceProviderType, on_delete=models.PROTECT)
    name                    = models.CharField(max_length=50)
    cnpj_cpf                = models.CharField(max_length=50)
    legal_person            = models.BooleanField(null=True, blank=False)
    cadastur                = models.CharField(max_length=50)
    email                   = models.EmailField(null=True, blank=False)
    cell_phone              = models.CharField(max_length=50)
    address                 = models.CharField(max_length=50)
    business_hours          = models.CharField(max_length=50)
    created_on              = models.DateTimeField(auto_now_add=True)
    modified_on             = models.DateTimeField(auto_now_add=True)
    active                  = models.BooleanField(default=True)
    registration_user       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    travel_agency           = models.ForeignKey(TravelAgency, on_delete=models.PROTECT)

    def __str__(self):
        return '%s' % (self.name)

class ServiceType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return '%s' % (self.name)


class Transport(models.Model):
    provider_service    = models.ForeignKey(ServiceProvider, on_delete=models.PROTECT)
    model               = models.CharField(max_length=50)
    brand               = models.CharField(max_length=50)    
    year                = models.IntegerField(null=True, blank=False)
    seats               = models.IntegerField(null=True, blank=False)
    bathroom            = models.BooleanField(default=False, null=True, blank=True)
    minibar             = models.BooleanField(default=False, null=True, blank=True)
    air_conditioning    = models.BooleanField(default=False, null=True, blank=True)
    sound               = models.BooleanField(default=False, null=True, blank=True)
    tv                  = models.BooleanField(default=False, null=True, blank=True)
    details             = models.CharField(max_length=200)
    created_on          = models.DateTimeField(auto_now_add=True)
    modified_on         = models.DateTimeField(auto_now_add=True)
    active              = models.BooleanField(default=True)
    registration_user   = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    travel_agency       = models.ForeignKey(TravelAgency, on_delete=models.PROTECT)

    def __str__(self):
        return '%s' % (self.model)


class Estimate(models.Model):
    excursion               = models.ForeignKey(Excursion, on_delete=models.PROTECT)
    service_provider_type   = models.ForeignKey(ServiceProviderType, on_delete=models.PROTECT)
    service_provider        = models.ForeignKey(ServiceProvider, on_delete=models.PROTECT)
    cost                    = models.IntegerField(null=False)
    start_time              = models.DateTimeField()
    end_time                = models.DateTimeField()
    selected                = models.BooleanField(default=False, null=True, blank=True)
    details                 = models.CharField(max_length=200)
    created_on              = models.DateTimeField(auto_now_add=True)
    modified_on             = models.DateTimeField(auto_now_add=True)
    active                  = models.BooleanField(default=True)
    registration_user       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    travel_agency           = models.ForeignKey(TravelAgency, on_delete=models.PROTECT)


class EstimateTransportDetails(models.Model):
    estimate  = models.ForeignKey(Estimate, on_delete=models.PROTECT)
    transport = models.ForeignKey(Transport, on_delete=models.PROTECT)


class TravelItinerary(models.Model):
    excursion           = models.ForeignKey(Excursion, on_delete=models.PROTECT)
    start_time          = models.DateTimeField()
    end_time            = models.DateTimeField()
    paid                = models.BooleanField(default=False, null=True, blank=True)
    inclusive           = models.BooleanField(default=False, null=True, blank=True)
    cost                = models.IntegerField(null=False)
    details             = models.CharField(max_length=200)
    created_on          = models.DateTimeField(auto_now_add=True)
    modified_on         = models.DateTimeField(auto_now_add=True)
    active              = models.BooleanField(default=True)
    registration_user   = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    travel_agency       = models.ForeignKey(TravelAgency, on_delete=models.PROTECT)
