from django.shortcuts import render
from django.http import HttpResponse
from .models import CentroMedico
from .serializers import CentroMedicoSerializer
from rest_framework import views
from rest_framework.response import Response
# Create your views here.

class ListaDeCentrosMedicos(views.APIView):
    
    def get(self, request, format=None):
        centros = CentroMedico.objects.all()
        datos_formateados = CentroMedicoSerializer(centros, many=True)
        return Response(datos_formateados.data) 
