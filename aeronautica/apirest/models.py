from django.db import models
from django.db.models.fields import CharField
from registros.models import *

class Piloto(models.Model):
    rut = models.CharField(primary_key=True, null=False, default=None, max_length=10)
    nombre = models.CharField(null=False, default=None, max_length=200)
    apellido = models.CharField(null=False, default=None, max_length=200)
    horas_vuelo_A = models.CharField(null=False, default=0, max_length=1000)
    horas_vuelos_E = models.CharField(null=False, default=0, max_length=1000)
    licencia_vencida = models.BooleanField(default=False)
    password = models.CharField(null= False, default=None, max_length=250)

    class Meta:
        db_table = 'piloto'
        ordering = ['rut']


class Consutor(models.Model):
    rut = models.CharField(primary_key=True, null=False, default=None, max_length= 10)
    password = models.CharField(null= False, default=None, max_length=250)


class Licencia(models.Model):
    n_licencia_piloto = models.ForeignKey(Piloto, on_delete=models.CASCADE, related_name='n_licencia')
    municipalidad = models.CharField(null=False, default=None, max_length=100)
    direccion = models.CharField(null=False, default=None, max_length=100)
    clase = models.CharField(null=False, default=None, max_length=1)
    fecha_ultimo_control = models.DateField(auto_now=False,auto_now_add=False)
    fecha_control = models.DateField(auto_now=False,auto_now_add=False)

    class Meta:
        db_table = 'Licencia'
        ordering = ['n_licencia_piloto']


class Aeronave(models.Model):
    matricula = models.CharField(primary_key=True, null=False, default=None, max_length=6)
    modelo = models.CharField(null=False, default=None, max_length=30)
    horas_vuelo = models.IntegerField(null=False, default=0)
    fecha_inspeccion_anual = models.DateField(auto_now=False,auto_now_add=False)
    fecha_aeronavegabilidad = models.DateField(auto_now=False,auto_now_add=False)
    ano_fabricacion = models.DateField(auto_now=False,auto_now_add=False)
    disponible = models.BooleanField(default=True)

    class Meta:
        db_table = 'Aeronave'
        ordering = ['matricula']



class Vuelo(models.Model):
    copiloto = models.ForeignKey(Piloto, on_delete=models.CASCADE, related_name='copiloto', default=None)
    piloto = models.ForeignKey(Piloto, on_delete=models.CASCADE, related_name='piloto', default=None)
    aeronave = models.ForeignKey(Aeronave, on_delete=models.CASCADE)
    condicion_vuelo = models.CharField(null = False, default=None, max_length=30)
    duracion_vuelo_p = models.IntegerField(default=0, null=False)
    duracion_vuelo_c = models.IntegerField(default=0, null=False)
    duracion_vuelo_total = models.IntegerField(default=0, null=False)
    origen = models.CharField(null = False, default=None, max_length=250)
    destino = models.CharField(null = False, default=None, max_length=250)
    mision_completada = models.BooleanField(default=False)

    class Meta:
        db_table = 'vuelos'
        ordering = ['id']



class Componente(models.Model):
    nombre_componente = models.CharField(null=False, default=None, max_length=200)
    tipo = models.CharField(null=False, default=None, max_length=30)
    aeronave = models.ForeignKey(Aeronave, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Componente'
        ordering = ['id']
