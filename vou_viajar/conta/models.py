"""
Models da aplicação 'conta'.
"""

import datetime
import re

from django.db import models
from django.core import validators
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings

class UserManager(BaseUserManager):
    
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(_('The given username must be set'))
            email = self.normalize_email(email)
            user = self.model(username=username, email=email,
            is_staff=is_staff, is_active=True,
            is_superuser=is_superuser, last_login=now,
            date_joined=now, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
        return user
        
    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False,
            **extra_fields)
    
    def create_superuser(self, username, email, password, **extra_fields):
        user=self._create_user(username, email, password, True, True, **extra_fields)
        user.is_active=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(_('username'), max_length=15, unique=False,
        help_text=_('Required. 15 characters or fewer. Letters, \
        numbers and @/./+/-/_ characters'),
    validators=[
        validators.RegexValidator(
        re.compile('^[\w.@+-]+$'),
        _('Enter a valid username.'),
        _('invalid'))])
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    email = models.EmailField(_('email'), max_length=255, unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as active. \
    Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_trusty = models.BooleanField(_('trusty'), default=False,
        help_text=_('Designates whether this user has confirmed his account.'))
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        
    def get_full_name(self):
            full_name = '%s %s' % (self.first_name, self.last_name)
            return full_name.strip()
    
    def get_short_name(self):
        return self.first_name
        
    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])


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
    usuario_cadastro = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    data_cadastro = models.DateTimeField(auto_now_add=True)


class ContatoAgencia(models.Model):

    email = models.EmailField(null=False, blank=False)
    contato = models.CharField(max_length=11)
    fan_page_oficial = models.URLField(null=True, blank=True)
    instagram_oficial = models.URLField(null=True, blank=True)
    site_oficial = models.URLField(null=True, blank=True)
    agencia = models.ForeignKey(Agencia, on_delete=models.PROTECT)


class Pessoa(models.Model):

    nome = models.CharField(
        max_length=100,
        null=False,
        blank=False, )
    cpf = models.CharField(max_length=14)
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    agencia = models.ForeignKey(Agencia, on_delete=models.PROTECT)

class ContatoPessoa(models.Model):

    email = models.EmailField(null=False, blank=False)
    contato = models.CharField(max_length=11)
    whatsapp = models.CharField(max_length=11)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)