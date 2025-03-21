from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListaDeDoctores.as_view(), name = 'Lista de Doctores')

]
