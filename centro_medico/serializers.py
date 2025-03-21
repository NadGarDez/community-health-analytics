from rest_framework import serializers
from .models import CentroMedico

class CentroMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroMedico
        fields = ['*']
