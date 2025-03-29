from django.db import models

# Create your models here.

class CentroMedico(models.Model):
    name = models.CharField(max_length = 20)
    info = models.JSONField()
    def __str__(self):
        return self.name
