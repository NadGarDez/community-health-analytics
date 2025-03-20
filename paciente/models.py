from django.db import models
from doctor.models import UsuarioPersonalizado

GRADOS_DISPENSARIALES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4')
)


class Paciente(models.Model):
    user = models.OneToOneField(UsuarioPersonalizado, on_delete=models.PROTECT)
    direccion= models.CharField(max_length=200) # en otras versiones podria tener un modelo aparte
    codigo_plus = models.CharField(max_length=10, null=True, blank=True)
    GD = models.CharField(
        max_length = 1,
        choices = GRADOS_DISPENSARIALES,
        default = 1
    ) 
