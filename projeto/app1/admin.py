from django.contrib import admin
from usuarios.models import Profissional, Paciente
from .models import pacientesAtivo,pesquisasAtiva
# Register your models here.
admin.site.register(Profissional)
admin.site.register(Paciente)
admin.site.register(pacientesAtivo)
admin.site.register(pesquisasAtiva)