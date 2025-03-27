from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from .serializers import ConsultaSerializer
from .models import Consulta

# Create your views here.

class ListaDeConsultas(APIView):

    def get(self,request):
        resultados = Consulta.objects.all()
        formato = ConsultaSerializer(resultados,many=True)
        return Response(formato.data)

class ListaDeConsultasPorDoctor(GenericAPIView,ListModelMixin):
    serializer_class = ConsultaSerializer
    
    def get_queryset(self):
        doctor_id = self.kwargs.get('doctor')
        return Consulta.objects.filter(doctor = doctor_id)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ListaDeConsultasPorCentro(GenericAPIView, ListModelMixin):
    serializer_class = ConsultaSerializer

    def get_queryset(self):
        centro_id = self.kwargs.get('centro')
        return Consulta.objects.filter(centro_medico = centro_id)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



class ListaDeConsultasPorDiagnostico(GenericAPIView, ListModelMixin):
    serializer_class = ConsultaSerializer

    def get_queryset(self):
        diagnostico_id = self.kwargs.get('diagnostico')
        return Consulta.objects.filter(diagnostico = diagnostico_id)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


