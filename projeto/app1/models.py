from django.db import models
from xmlrpc.client import Boolean
from django.contrib.auth.models import User
from django.conf import settings
from usuarios.models import Profissional, Paciente


# Create your models here.
class pesquisasAtiva (models.Model):
    CAAE = models.CharField(max_length=25)
    Profissional = models.ForeignKey(Profissional,on_delete=models.CASCADE)
    TCLE= models.TextField()
    TImagemVoz= models.TextField()

class pacientesAtivo(models.Model):
    Profissional = models.ForeignKey(Profissional,on_delete=models.CASCADE)
    Paciente = models.ForeignKey(Paciente,on_delete=models.CASCADE)
    PacienteEscutou= models.BooleanField (default=False)
    PacienteAutorizouImagem = models.BooleanField (default=False)
    PacienteAutorizouVoz = models.BooleanField (default=False)
    PacienteAutorizouVideo = models.BooleanField (default=False)
    PacienteAutorizouPesquisa = models.BooleanField (default=False)






