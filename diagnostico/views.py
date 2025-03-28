from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Diagnostico
from .serializers import DiagnosticoSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

# Create your views here.

def index(request):
    return HttpResponse('App diagnostico')

class CreacionDeDiagnostico(GenericAPIView, CreateModelMixin):
    serializer_class = DiagnosticoSerializer
    def post(self,request,  *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ListaDeDiagnosticos(APIView):
    
    def get(self, request, *args, **kwargs):
        resultados = Diagnostico.objects.all()
        formato = DiagnosticoSerializer(resultados, many = True) 
        return Response(formato.data)


class ListaDeDiagnosticosPorCreador(GenericAPIView, ListModelMixin):
    serializer_class = DiagnosticoSerializer

    def get_queryset(self):
        doctor = self.kwargs.get('doctor')
        return  Diagnostico.objects.filter(creador = doctor)


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


