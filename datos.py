import RPi.GPIO as gpio 
import Adafruit_DHT as dht
from time import sleep 
import datetime
#import data_sqlite
import sqlite3
import requests 


try:
	data_sqlite.crear_database()
except:
	pass


#conn=data_sqlite.crear_conexion("database1.db")	
	
led_r = 23

led_y = 24

led_g = 25

gpio.setmode(gpio.BCM)

gpio.setup(led_r,gpio.OUT)

gpio.setup(led_y,gpio.OUT)

gpio.setup(led_g,gpio.OUT)


led_list = [led_r,led_y,led_g]

led_time = 0.05

def DHT11_data():

	humi, temp = dht.read_retry(dht.DHT11, 18)
	date_time = datetime.datetime.now()
	
	return humi, temp, 0

while True:

	try:

		humedad, temperatura, tiempo = DHT11_data()
		datos = {"Temperatura": temperatura, "Humedad": humedad, "tiempo": tiempo} #le digo que me escriba la temp y humed diccionario

		with open("datos.json", "w") as archivo: # Escribe el archivo de datos
			archivo.writelines([str(datos).replace("'",'"')])	# Escribe el diccionario 'datos'

		try:
			requests.post("http://3.13.8.229:8000/add-data", json={'Temperatura': temperatura, 'Humedad':  humedad})
		except:
			print("################ LOST CONNECTION #################")
			print("Humedad", humedad, "Temperatura", temperatura)
			pass

		sql = "INSERT INTO Ara_project_web_datos (temperatura, humedad) values ({0},{1});".format(temperatura, humedad)
		print(sql)                       
		conn=sqlite3.connect("db.sqlite3")
		with conn:
			cur = conn.cursor()
			cur.execute(sql)
		
		
		
		if humedad > 50.0:

			gpio.output(led_r, True)

			gpio.output(led_g, False)

		else:

			gpio.output(led_r, False)

			gpio.output(led_g, True)

		sleep(10)
		

	except KeyboardInterrupt:

		gpio.clean()

		print("Programa terminado")

		break

