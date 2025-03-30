from django.urls import path
from . import views 

urlpatterns = [
    path('', views.ListaDeCentrosMedicos.as_view(), name='lista_de_centros'),
    path('doctor/<int:doctor>/', views.ListaDeCentrosMedicosPorDoctor.as_view(), name='Lista_de_Centros_por_Doctor'),
    path('diagnostico/<int:diagnostico>/', views.ListaDeCentrosMedicosPorDiagnostico.as_view(), name='lista_de_Centros_por_Diagnostico'),
    path('crear/', views.CreacionDeCentroMedico.as_view(), name='Creacion_De_Centro_Medico')
]
