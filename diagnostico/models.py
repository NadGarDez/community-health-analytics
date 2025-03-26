from django.db import models
from doctor.models import Doctor

# Create your models here.

class Diagnostico(models.Model):
    nombre = models.CharField(max_length=200)
    detalle = models.TextField(null=True, blank=True)
    creador = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    def __str__(self):
        return self.nombre
