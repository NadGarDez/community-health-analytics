from django.db import models
from django.contrib.auth.models import AbstractUser
from centro_medico.models import CentroMedico

OPCIONES_DE_SEXO = (
    ('M','MASCULINO'),
    ('F','FEMENINO')

)


class UsuarioPersonalizado(AbstractUser):
    nombre = models.CharField(max_length=20, null= True, blank=True)
    segundo_nombre = models.CharField(max_length=20, null=True, blank=True)
    apellido = models.CharField(max_length=20,null= True, blank=True)
    segundo_apellido = models.CharField(max_length=20, null=True, blank=True)
    nacimiento = models.DateField(null= True, blank=True)
    prefijo_ci = models.CharField(max_length=1,null= True, blank=True)
    ci = models.CharField(max_length=10, null= True, blank=True)
    sexo = models.CharField(
        max_length=2,
        choices = OPCIONES_DE_SEXO,
        default = 'F'
    )


class Doctor(models.Model):
    user = models.OneToOneField(UsuarioPersonalizado, on_delete=models.PROTECT)
    centro_medico = models.ForeignKey(CentroMedico, on_delete=models.PROTECT, related_name='doctores')  


