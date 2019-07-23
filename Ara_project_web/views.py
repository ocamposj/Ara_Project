from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Datos
import json
import sqlite3

def home(request):
    info = Datos.objects.last()
    Tempe = info.temperatura
    Hume = info.humedad
    dict = {"Temperatura":Tempe,"Humedad":Hume}
    print("tempe",Tempe, "hume",Hume) #consultamos la BD y guardamos todos
    return render(request, 'home.html', dict) #Los datos se agregan despues del html

@csrf_exempt
def add_data(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        temperatura = json_data['Temperatura']
        humedad = json_data['Humedad']
        print("Humedad", humedad, "Temperatura", temperatura)

        sql = "INSERT INTO Ara_project_web_datos (temperatura, humedad) values ({0},{1});".format(temperatura, humedad)
        conn=sqlite3.connect("db.sqlite3")
        with conn:
            cur = conn.cursor()
            cur.execute(sql)
    return HttpResponse(status=200)
