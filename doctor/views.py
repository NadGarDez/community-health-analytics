from django.shortcuts import render
from django.http import HttpResponse
from .models import Doctor
from .serializers import DoctorSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework import views
from rest_framework.response import Response
#

# Create your views here.

class ListaDeDoctores(views.APIView):
    def get(self, request, format = None):
        resultado = Doctor.objects.all()
        formato = DoctorSerializer(resultado, many = True)
        return Response(formato.data)


class ListaDeDoctoresPorCentro(GenericAPIView,ListModelMixin):
    serializer_class = DoctorSerializer
    def get_queryset(self):
        return Doctor.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs) 


class ListaDeDoctoresPorPaciente(GenericAPIView, ListModelMixin):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        return Doctor.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ListaDeDoctoresPorDiagnosticoEnConsultas(GenericAPIView, ListModelMixin):

    serializer_class = DoctorSerializer

    def get_queryset(self):

        return Doctor.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

