from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListaDeDiagnosticos.as_view(), name='Lista de Diagnosticos'),
    path('creador/<int:doctor>/', views.ListaDeDiagnosticosPorCreador.as_view(), name='Lista de Diagnosticos'),
    path('crear', views.CreacionDeDiagnostico.as_view(), name = 'Creacion De Diagnostico')
]
