from django.db import models
from paciente.models import Paciente
from diagnostico.models import Diagnostico
from django.utils import timezone
from doctor.models import Doctor
# Create your models here.

CONSULTAS = (
    (1, 'Morbilidad'),
    (2, 'Visita de Campo')
)


class Consulta(models.Model):
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.PROTECT)
    paciente = models.ForeignKey(Paciente, on_delete= models.PROTECT)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    doctor = models.ForeignKey(Doctor, on_delete = models.PROTECT)
    tipo = models.TextField(
        max_length = 1,
        choices = CONSULTAS,
        default = 1
    )
