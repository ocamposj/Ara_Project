import RPi.GPIO as gpio 
import Adafruit_DHT as dht
from time import sleep 
import datetime
#import data_sqlite
import sqlite3

try:
	data_sqlite.crear_database()
except:
	pass

#conn=data_sqlite.crear_conexion("database1.db")	

gpio.setmode(gpio.BCM)

def DHT11_data():

	humi, temp = dht.read_retry(dht.DHT11, 18)
	time = datetime.datetime.now()
	
	return humi, temp, time

while True:

	try:

		humedad, temperatura, tiempo = DHT11_data()
		datos = {"Temperatura": temperatura, "Humedad": humedad, "tiempo": tiempo} #le digo que me escriba la temp y humed diccionario

		sql = "INSERT INTO Ara_project_web_datos (temperatura, humedad) values ({0},{1});".format(temperatura, humedad)
		print(sql)                       
		conn=sqlite3.connect("db.sqlite3")
		with conn:
			cur = conn.cursor()
			cur.execute(sql)

		sleep(15)

	except KeyboardInterrupt:

		gpio.clean()

		print("Programa terminado")

		break