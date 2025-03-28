from django.shortcuts import render
from django.http import HttpResponse
from .models import CentroMedico
from doctor.models import Doctor
from .serializers import CentroMedicoSerializer
from rest_framework import views
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
# Create your views here.

class CreacionDeCentroMedico(GenericAPIView, CreateModelMixin):
    serializer_class = CentroMedicoSerializer
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ListaDeCentrosMedicos(views.APIView):
    
    def get(self, request, format=None):
        centros = CentroMedico.objects.all()
        datos_formateados = CentroMedicoSerializer(centros, many=True)
        return Response(datos_formateados.data) 

class ListaDeCentrosMedicosPorDoctor(GenericAPIView, ListModelMixin):
    serializer_class = CentroMedicoSerializer

    def get_queryset(self):
        try:
            doctor = self.kwargs.get('doctor')
            return Doctor.objects.get(pk = doctor).centro_medico.all()
        except Doctor.DoesNotExist:
            return None #print some error

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



class ListaDeCentrosMedicosPorDiagnostico(GenericAPIView, ListModelMixin):
    serializer_class = CentroMedicoSerializer

    def get_queryset(self):
        try:
            diagnostico = self.kwargs.get('diagnostico')
            return CentroMedico.objects.filter(consultas__diagnostico__pk = diagnostico)
        except:
            return None


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



