from django.shortcuts import render
from django.http import HttpResponse
from .models import Datos

def home(request):
    #listita = Datos.objects.all() #consultamos la BD y guardamos todos
    return render(request, 'home.html') #Los datos se agregan despues del html

def data_from_sensor(request):
    with open("datos.json", "r") as archivo:
        resultados = archivo.readlines()

    return render(request, "sensor_data.html", resultados)
