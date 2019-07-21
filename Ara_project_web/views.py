from django.shortcuts import render
from django.http import HttpResponse
#from .models import Datos
import json

def home(request):
    #listita = Datos.objects.all() #consultamos la BD y guardamos todos
    return render(request, 'home.html') #Los datos se agregan despues del html

def data_from_sensor(request):
    with open("/home/pi/Desktop/Ara_Project/Ara_project_web/datos.json", "r") as archivo:
        datos = json.load(archivo)
        print (datos) #FUNCIONA :')-

    return render(request, "sensor_data.html", datos)

