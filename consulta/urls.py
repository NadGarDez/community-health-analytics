from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListaDeConsultas.as_view(), name='Lista de Consultas')

]
