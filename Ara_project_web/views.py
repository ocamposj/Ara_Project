from django.shortcuts import render
from django.http import HttpResponse
from .models import Datos

def home(request):
    return HttpResponse("<h1 Style = 'color': black> Homepage </h1>")
    #listita = Datos.objects.all() #consultamos la BD y guardamos todos
    #return render(request, 'x.html', listita) #Los datos se agregan despues del html



