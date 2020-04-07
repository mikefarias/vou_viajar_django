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
    
    username    = models.CharField(_('username'), max_length=15, unique=False,
        help_text=_('Required. 15 characters or fewer. Letters, \
        numbers and @/./+/-/_ characters'),
    validators=[
        validators.RegexValidator(
        re.compile('^[\w.@+-]+$'),
        _('Enter a valid username.'),
        _('invalid'))])
    first_name  = models.CharField(_('first name'), max_length=30)
    last_name   = models.CharField(_('last name'), max_length=30)
    email       = models.EmailField(_('email'), max_length=255, unique=True)
    is_staff    = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin site.'))
    is_active   = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as active. \
    Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_trusty   = models.BooleanField(_('trusty'), default=False,
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


class ContactTravelAgency(models.Model):
    
    email               = models.EmailField(null=False, blank=False)
    phone_number        = models.CharField(max_length=11)
    whatsapp            = models.CharField(max_length=11)
    fan_page            = models.URLField(null=True, blank=True)
    instagram           = models.URLField(null=True, blank=True)
    website             = models.URLField(null=True, blank=True)
    created_on          = models.DateTimeField(auto_now_add=True)
    modified_on         = models.DateTimeField(auto_now_add=True)
    active              = models.BooleanField(default=True)


class TravelAgency(models.Model):
    """
    A class Agencia representa uma agência turística.
    """
    name                = models.CharField(max_length=50, null=False, blank=False)
    code_cadastur       = models.CharField(max_length=10, null=False, blank=False)
    cnpj                = models.CharField(max_length=14)
    logo                = models.ImageField(upload_to='img/logo_agency', null=True, blank=True)
    physical_agency     = models.BooleanField(null=False, blank=False)
    address             = models.CharField(max_length=200)
    owner               = models.ForeignKey(User, on_delete=models.PROTECT)
    contact             = models.OneToOneField(ContactTravelAgency, on_delete=models.SET_NULL, null=True)
    created_on          = models.DateTimeField(auto_now_add=True)
    modified_on         = models.DateTimeField(auto_now_add=True)
    active              = models.BooleanField(default=True)


class Profile(models.Model):
    
    cpf_cnpj            = models.CharField(max_length=14)
    profile_photo       = models.ImageField(upload_to='img/profile', null=True, blank=True)
    phone_number        = models.CharField(max_length=11)
    whatsapp            = models.CharField(max_length=11)
    user                = models.ForeignKey(User, on_delete=models.PROTECT)
    agency_travel       = models.ForeignKey(TravelAgency, on_delete=models.PROTECT)
    created_on          = models.DateTimeField(auto_now_add=True)
    modified_on         = models.DateTimeField(auto_now_add=True)
    active              = models.BooleanField()