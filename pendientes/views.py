from django.shortcuts import render
from django.http import HttpResponse
from pendientes.models import Tarea #Importamos las tareas de models
# Create your views here.

def index(request):
    listita = Tarea.objects.all() #consultamos la Base de Datos y guardamos 
                                  #TODOS(all) los registros de la tabla Tarea como
                                  #objetos y guardamos en la listita.
    persona = {
        "nombre": "Sebas",
        "edad": 23,
        "hobbies": ["Fulbo", "Diseno","Save the world (?)"],
        "lista_tareas": listita
    }
    return render(request, "dia8.html", persona) #retornamos el saludo
#Ejercicio 1
def tarea(request):
    return HttpResponse("Hola, soy la vista tarea")

#Ejercicio 2
def respuestas(request):
    return HttpResponse("Sobre nosotros: ...")


#Ejercicio 1
#Crear la vista/funcion tarea y conectar con la direccion 
#/tareas en el archivo urls.py
#despues ir al navegador y abrir http://....../tareas

#Ejercicio2
#Crear una vista respuestas que retorne un texto cuando 
# en el navegador entremos a http://..../info
#Pista: crear la funcion /vista en views.py y conectar en 
#urls.py usando path (....)

