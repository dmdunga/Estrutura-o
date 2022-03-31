from django.contrib import admin
from .models import profissional, paciente,pacientesAtivo,pesquisasAtiva
# Register your models here.
admin.site.register(profissional)
admin.site.register(paciente)
admin.site.register(pacientesAtivo)
admin.site.register(pesquisasAtiva)