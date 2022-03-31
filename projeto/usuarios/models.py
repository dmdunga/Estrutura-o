from django.db import models
import re
import secrets
import yagmail
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from datetime import date
from datetime import datetime
from django.utils import timezone
from django.core import validators
from django.conf import settings

# python manage.py migrate admin zero
# python manage.py migrate auth zero
# python manage.py migrate contenttypes zero
# python manage.py migrate sessions zero
# python manage.py makemigrations usuarios
# python manage.py migrate usuarios
# python manage.py migrate
# python manage.py createsuperuser
# python manage.py runserver

# Create your models here.


class UserManager(BaseUserManager):
    def _create_user(self, username, password, is_staff, is_superuser, **extra_fields):
        now = datetime.now()
        if not username:
            raise ValueError(('The given username must be set'))
        # email = self.normalize_email(email)
        user = self.model(username=username, password=password, is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, **extra_fields):
        # print("Criou Usuário: ", username)
        return self._create_user(username, password, False, False, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        user = self._create_user(
            username, password, True, True, **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    CHOICES = [('1', 'Feminine'), ('2', 'Masculine'), ('3', 'Other')]
    first_name = models.CharField(('first name'), max_length=30)
    last_name = models.CharField(('last name'), max_length=30)
    email = models.EmailField(('email address'), max_length=255, unique=True)
    CPF = models.CharField(('CPF'), max_length=25)
    cnpj = models.CharField(('cnpj'), max_length=25, default=False)
    cep = models.CharField(('cep'), max_length=25, default=False)
    rua = models.CharField(('rua'), max_length=25, default=False)
    numero = models.CharField(('numero'), max_length=10, default=False)
    complemento = models.CharField(
        ('complemento'), max_length=50, default=False)
    bairro = models.CharField(('bairro'), max_length=25, default=False)
    cidade = models.CharField(('cidade'), max_length=25, default=False)
    estado = models.CharField(('estado'), max_length=25, default=False)
    BithDate = models.DateField(default=date.today, verbose_name="Bith date")
    Phone = models.CharField(max_length=15)
    username = models.CharField(('username'), max_length=15, unique=True, help_text=('Required. 15 characters or fewer. Letters, numbers and @/./+/-/_ characters'),
                                validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'), ('Enter a valid username.'), ('invalid'))])
    password = models.CharField(('password'), max_length=128)
    Gender = models.CharField(max_length=14, choices=CHOICES)

    is_staff = models.BooleanField(('staff status'), default=False, help_text=(
        'Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(('active'), default=False, help_text=(
        'Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))

    date_joined = models.DateTimeField(('date joined'), default=timezone.now)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

class Paciente(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,unique=True)
    activation_token = models.CharField(max_length=67, unique=True,default=secrets.token_urlsafe(50))
    is_token_validated = models.BooleanField()
    is_token_validated = False

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

class Profissional(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,unique=True)
    Profissao=models.TextField()
    numeroDeRegistroProfissional = models.TextField()
    
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
