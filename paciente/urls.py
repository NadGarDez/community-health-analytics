from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListaDePacientes.as_view(), name='Lista de Pacientes')

]






