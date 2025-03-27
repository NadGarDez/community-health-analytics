from django.shortcuts import render
from django.http import HttpResponse
from .models import Paciente 
from .serializers import PacienteSerializer
from rest_framework import views
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
# Create your views here.

class ListaDePacientes(views.APIView):
    
    def get(self, request, format=None):
        centros = Paciente.objects.all()
        datos_formateados = PacienteSerializer(centros, many=True)
        return Response(datos_formateados.data) 


class ListaDePacientesPorCentro(GenericAPIView, ListModelMixin):
    serializer_class =  PacienteSerializer  
    def get_queryset(self):
        centro = self.kwargs.get('centro')
        return Paciente.objects.filter(consultas__centro__pk = centro)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ListaDePacientesPorDoctor(GenericAPIView, ListModelMixin):
    serializer_class = PacienteSerializer
    def get_queryset(self):
        doctor = self.kwargs.get('doctor')
        return Paciente.objects.filter(consultas__doctor__pk = doctor)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ListaDePacientesPorDiagnostico(GenericAPIView, ListModelMixin):
    serializer_class = PacienteSerializer
    def get_queryset(self):
        diagnostico = self.kwargs.get('diagnostico')
        return Paciente.objects.filter(consultas__diagnostico__pk = diagnostico)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

