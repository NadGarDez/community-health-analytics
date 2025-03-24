from django.db import models
from paciente.models import Paciente
from diagnostico.models import Diagnostico
from django.utils import timezone
from doctor.models import Doctor
from centro_medico.models import CentroMedico
# Create your models here.

CONSULTAS = (
    (1, 'Morbilidad'),
    (2, 'Visita de Campo')
)

PRIMARIA_O_SUCESIVA = (
    ('P', 'Primaria'),
    ('S', 'Sucesiva')
)
class Conducta(models.Model):
    nombre = models.CharField(max_length = 25)
    detalle = models.CharField(max_length = 200)

class Consulta(models.Model):
    centro_medico = models.ForeignKey(CentroMedico, on_delete = models.PROTECT, related_name='consultas')
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.PROTECT,  related_name='consultas')
    paciente = models.ForeignKey(Paciente, on_delete= models.PROTECT,  related_name='consultas')    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    doctor = models.ForeignKey(Doctor, on_delete = models.PROTECT,  related_name='consultas')
    tipo = models.TextField(
        max_length = 1,
        choices = CONSULTAS,
        default = 1
    )
    conducta = models.ForeignKey(Conducta, on_delete = models.PROTECT)
    PS = models.TextField(
        max_length = 1,
        choices = PRIMARIA_O_SUCESIVA,
        default = 'P'
    )

