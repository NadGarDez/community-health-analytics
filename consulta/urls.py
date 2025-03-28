from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListaDeConsultas.as_view(), name='Lista de Consultas'),
    path('doctor/<int:doctor>/', views.ListaDeConsultasPorDoctor.as_view(), name='Lista de Consultas por Doctor'),
    path('centro/<int:centro>/', views.ListaDeConsultasPorCentro.as_view(), name='Lista de consultas por centro'),
    path('diagnostico/<int:diagnostico>/', views.ListaDeConsultasPorDiagnostico.as_view(), name='Lista de consultas por diagnostico'),
    path('crear/', views.CreacionDeConsulta.as_view(), name = 'Creacion de Consultaa')
]
