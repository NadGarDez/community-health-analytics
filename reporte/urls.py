from django.urls import path
from . import views

urlpatterns = [
    path('', views.Reportes.as_view(), name = 'Reportes')
]
