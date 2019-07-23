from django.db import models

# Create your models here.

class Datos (models.Model):
    temperatura = models.CharField(max_length = 100, blank=True, null=True)
    presion_atm = models.CharField(max_length = 100, blank=True, null=True)
    humedad = models.CharField(max_length = 100, blank=True, null=True)
    dir_viento = models.CharField(max_length = 100, blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Datos"



