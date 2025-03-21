from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ConsultaSerializer
from .models import Consulta

# Create your views here.

class ListaDeConsultas(APIView):

    def get(self, *args, **kwargs):
        resultados = Consulta.objects.all()
        formato = ConsultaSerializer(resultados,many=True)
        return Response(formato.data)

