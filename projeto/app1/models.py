from django.db import models
from xmlrpc.client import Boolean
from django.contrib.auth.models import User

# Create your models here.
class profissional (models.Model):
    name= models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name
    pass

class paciente (models.Model):
    name= models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name
    pass

class pesquisasAtiva (models.Model):
    CAAE = models.CharField(max_length=25)
    Profissional = models.ForeignKey(profissional,on_delete=models.CASCADE)
    TCLE= models.TextField()
    TImagemVoz= models.TextField()

class pacientesAtivo(models.Model):
    Profissional = models.ForeignKey(profissional,on_delete=models.CASCADE)
    Paciente = models.ForeignKey(paciente,on_delete=models.CASCADE)
    PacienteEscutou= models.BooleanField (default=False)
    PacienteAutorizouImagem = models.BooleanField (default=False)
    PacienteAutorizouVoz = models.BooleanField (default=False)
    PacienteAutorizouVideo = models.BooleanField (default=False)
    PacienteAutorizouPesquisa = models.BooleanField (default=False)






