from django.urls import path
from . import views

urlpatterns = [
        path('', views.ListaDeDoctores.as_view(), name = 'Lista de Doctores'),
    path('centro/<int:centro>/', views.ListaDeDoctoresPorCentro.as_view(), name = 'Lista de Doctores por Centro'),
    path('paciente/<int:paciente>/', views.ListaDeDoctoresPorPaciente.as_view(), name = 'Lista de Doctores por Paciente'),
    path('diagnostico/<int:diagnostico>/', views.ListaDeDoctoresPorDiagnosticoEnConsultas.as_view(), name = 'Lista de Doctores por Diagnostico en consultas')
]
