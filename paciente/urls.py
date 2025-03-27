from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListaDePacientes.as_view(), name='Lista de Pacientes'),
    path('centro/<int:centro>/', views.ListaDePacientesPorCentro.as_view(), name='Lista de Pacientes por Centro'),
    path('doctor/<int:doctor>/', views.ListaDePacientesPorDoctor.as_view(), name='Lista de Pacientes por Doctor'),
    path('diagnostico/<int:diagnostico>/', views.ListaDePacientesPorDiagnostico.as_view(), name='Lista de Pacientes por Diagnostico')
]

