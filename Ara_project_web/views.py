from django.shortcuts import render
from django.http import HttpResponse
from .models import Datos

def home(request):
    #listita = Datos.objects.all() #consultamos la BD y guardamos todos
    return render(request, 'home.html') #Los datos se agregan despues del html



