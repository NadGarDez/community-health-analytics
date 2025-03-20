from django.db import models
from django.contrib.auth.models import AbstractUser


OPCIONES_DE_SEXO = (
    ('M','MASCULINO'),
    ('F','FEMENINO')

)


class UsuarioPersonalizado(AbstractUser):
    nombre = models.CharField(max_length=20)
    segundo_nombre = models.CharField(max_length=20, null=True, blank=True)
    apellido = models.CharField(max_length=20)
    segundo_apellido = models.CharField(max_length=20, null=True, blank=True)
    nacimiento = models.DateField()
    prefijo_ci = models.CharField(max_length=1)
    ci = models.CharField(max_length=10)
    sexo = models.CharField(
        max_length=2,
        choices = OPCIONES_DE_SEXO,
        default = 'F'
    )


class Doctor(models.Model):
    user = models.OneToOneField(UsuarioPersonalizado, on_delete=models.PROTECT)
    


# Create your models here.
