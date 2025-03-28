from django.urls import path
from . import views 

urlpatterns = [
    path('', views.ListaDeCentrosMedicos.as_view(), name='lista_de_centros'),
    path('doctor/<int:doctor>/', views.ListaDeCentrosMedicosPorDoctor.as_view(), name='Lista de Centros por Doctor'),
    path('diagnostico/<int:diagnostico>/', views.ListaDeCentrosMedicosPorDiagnostico.as_view(), name='lista de Centros por Diagnostico'),
    path('create/', views.CreacionDeCentroMedico.as_view, name='Creacion De Centro Medico')
]
