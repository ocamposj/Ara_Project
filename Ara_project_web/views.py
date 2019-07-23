from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

#from .models import Datos
import json

def home(request):
    #listita = Datos.objects.all() #consultamos la BD y guardamos todos
    with open("/home/pi/Desktop/Ara_Project/datos.json", "r") as archivo:
        datos = json.load(archivo) #FUNCIONA :')-
    return render(request, 'home.html', datos) #Los datos se agregan despues del html
@csrf_exempt
def add_data(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        print(json_data)
    return HttpResponse(status=200)
