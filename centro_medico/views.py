from django.shortcuts import render
from django.http import HttpResponse
from .models import CentroMedico
from .serializers import CentroMedicoSerializer
from rest_framework import views
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
# Create your views here.

class ListaDeCentrosMedicos(views.APIView):
    
    def get(self, request, format=None):
        centros = CentroMedico.objects.all()
        datos_formateados = CentroMedicoSerializer(centros, many=True)
        return Response(datos_formateados.data) 

class ListaDeCentrosMedicosPorDoctor(GenericAPIView, ListModelMixin):
    serializer_class = CentroMedicoSerializer

    def get_queryset(self):
        return CentroMedico.objects.all()


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



class ListaDeCentrosMedicosPorDiagnostico(GenericAPIView, ListModelMixin):
    serializer_class = CentroMedicoSerializer

    def get_queryset(self):
        return CentroMedico.objects.all()


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



