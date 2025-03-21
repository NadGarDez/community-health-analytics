from django.shortcuts import render
from django.http import HttpResponse
from .models import Paciente 
from .serializers import PacienteSerializer
from rest_framework import views
from rest_framework.response import Response
# Create your views here.

class ListaDePacientes(views.APIView):
    
    def get(self, request, format=None):
        centros = Paciente.objects.all()
        datos_formateados = PacienteSerializer(centros, many=True)
        return Response(datos_formateados.data) 
