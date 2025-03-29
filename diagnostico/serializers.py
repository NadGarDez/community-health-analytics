from rest_framework.serializers import ModelSerializer
from .models import Diagnostico

class DiagnosticoSerializer(ModelSerializer):
    class Meta:
        model = Diagnostico
        fields = '__all__'

