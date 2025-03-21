from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporte
from .serializers import ReporteSerializer 
from rest_framework import views
from rest_framework.response import Response
# Create your views here.

class Reportes(views.APIView):
    
    def get(self, request, format=None):
        resultados = Reporte.objects.all()
        datos_formateados = ReporteSerializer(resultados,many=True)
        return Response(datos_formateados.data)
