from django.db import models

# Create your models here.

class Datos (models.Model):
    temperatura = models.CharField(max_length = 100)
    presion_atm = models.CharField(max_length = 100)
    humedad = models.CharField(max_length = 100)
    dir_viento = models.CharField(max_length = 100)
    creado = models.DateTimeField(auto_now_add=True)



