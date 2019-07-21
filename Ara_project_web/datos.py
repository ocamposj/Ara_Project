import RPi.GPIO as gpio 
import Adafruit_DHT as dht
from time import sleep 

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

	return humi, temp

while True:

	try:

		humedad, temperatura = DHT11_data()
		datos = {"Temperatura": temperatura, "Humedad": humedad} #le digo que me escriba la temp y humed diccionario

		with open("datos.json", "w") as archivo: # Escribe el archivo de datos
			archivo.writelines([str(datos).replace("'",'"')])	# Escribe el diccionario 'datos'

		print("Humedad", humedad, "Temperatura", temperatura)

		if humedad > 50.0:

			gpio.output(led_r, True)

			gpio.output(led_g, False)

		else:

			gpio.output(led_r, False)

			gpio.output(led_g, True)

		sleep(20)
		

	except KeyboardInterrupt:

		gpio.clean()

		print("Programa terminado")

		break
