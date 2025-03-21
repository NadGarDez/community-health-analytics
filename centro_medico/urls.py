from django.urls import path
from . import views 

urlpatterns = [
    path('', views.ListaDeCentrosMedicos.as_view(), name='lista_de_centros')
]
