from django.db import models

# Create your models here.


class Reporte(models.Model):
    reporte = models.FileField(upload_to ='uploads/% Y/% m/% d/')  
