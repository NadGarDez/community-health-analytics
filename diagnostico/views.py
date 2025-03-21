from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Diagnostico
from .serializers import DiagnosticoSerializer

# Create your views here.

def index(request):
    return HttpResponse('App diagnostico')

class ListaDeDiagnosticos(APIView):
    
    def get(self, *args, **kwargs):
        resultados = Diagnostico.objects.all()
        formato = DiagnosticoSerializer(resultados, many = True) 
        return Response(formato.data)


