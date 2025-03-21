from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListaDeDiagnosticos.as_view(), name='Lista de Diagnosticos')

]
