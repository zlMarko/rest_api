from django.db import models
from django.db.models.fields import CharField




class Piloto(models.Model):
    rut = models.CharField(null=False, default=None, max_length=10) 
    nombre = models.CharField(null=False, default=None, max_length = 200) 
    apellido = models.CharField(null=False, default= None, max_length = 200)
    licencia = models.CharField(null=False, default = None, max_length = 1)
    horas_vuelo = models.CharField(null=False, default=None, max_length = 1000)
    licencia_vencida = models.BooleanField(default=False)


    class Meta:
        db_table = 'piloto'
        ordering = ['id']



class Aeronave(models.Model):

    class Meta:
        db_table = 'aeronave'
        ordering = ['id']

