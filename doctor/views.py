from django.shortcuts import render
from django.http import HttpResponse
from .models import Doctor
from .serializers import DoctorSerializer
from rest_framework import views
from rest_framework.response import Response
#

# Create your views here.

class ListaDeDoctores(views.APIView):
    def get(self, request, format = None):
        resultado = Doctor.objects.all()
        formato = DoctorSerializer(resultado, many = True)
        return Response(formato.data)
