from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import CentroMedico as CM
from doctor.models import UsuarioPersonalizado, Doctor
from diagnostico.models import Diagnostico
from consulta.models import Consulta, Conducta
from paciente.models import Paciente
# Create your tests here.

class CentroMedico(APITestCase):
    item = None
    def setUp(self):
        # start user creation
        self.usuario1 = UsuarioPersonalizado(nombre='Iranad') 
        self.usuario1.save()

        self.usuario2 = UsuarioPersonalizado(nombre='Josue', username = 'josue') 
        self.usuario2.save()

        # end user creation
        # start medical center creation
        self.item = CM(name = 'example', info='exampleDetail') 
        self.item.save()
        # end medical center creation
        # start doctor creation
        self.doctor = Doctor(user=self.usuario1)
        self.doctor.save()
        self.doctor.centro_medico.set([self.item])
        
        self.diagnostico =  Diagnostico(nombre= 'x', creador = self.doctor)
        self.diagnostico.save()

        self.conducta = Conducta(nombre = 'conducta 1', detalle = 'detallle conducta 1')
        self.conducta.save()

        self.paciente = Paciente(user=self.usuario2, codigo_plus='123', GD=1)
        self.paciente.save()

        self.consulta = Consulta(centro_medico = self.item, diagnostico= self.diagnostico, paciente = self.paciente, doctor = self.doctor, conducta = self.conducta)
        self.consulta.save()

        

    def test_crear_centro_medico(self):
        url = reverse('Creacion_De_Centro_Medico')
        data = {
            'name': 'test name',
            'info': 'test info'
        }
        resultado= self.client.post(url, data, format='json')

        self.assertEqual(resultado.status_code, status.HTTP_201_CREATED)
        
    def test_lista_de_centros_medicos(self):

        url = reverse('lista_de_centros')

        resultado = self.client.get(url, format='json')

        self.assertEqual(len(resultado.data), 1)

    def test_lista_de_centros_medicos_por_doctor(self):
        url = reverse('Lista_de_Centros_por_Doctor', kwargs={'doctor':self.doctor.pk})
        resultado = self.client.get(url, format='json')
        self.assertEqual(len(resultado.data), 1)
    
    def test_lista_de_centros_medicos_por_diagnostico(self):
        url = reverse('lista_de_Centros_por_Diagnostico', kwargs={'diagnostico':self.diagnostico.pk})
        resultado = self.client.get(url, format='json')
        self.assertEqual(len(resultado.data), 1)
