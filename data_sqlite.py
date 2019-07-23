import sqlite3
from sqlite3 import Error
from Ara_project_web.datos import DHT11_data
import time

def crear_conexion(db_file):
    """ crear una conexion a una base de datos de SQlite  """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
    return None

def crear_tabla(conn, crear_tabla_sql):
    """ crear una tabla con el argumento crear_tabla"
    :param conn: Connection object
    :param crear_tabla_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor() #Cursor es un objeto
        c.execute(crear_tabla_sql)
        return c.lastrowid #Para obtener un id generado
    except Error as e:
        print(e)

def insertar_datos(conn, mediciones):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO datos(fecha, 
                                temperatura,
                                humedad,
                                presion_atmosferica,
                                radiacion_solar,
                                velocidad_viento,
                                direccion_viento,
                                cobertura_nubes,
                                precipitacion,
                                ozono_troposferico,
                                vapor_agua)
              VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql,mediciones)
    return cur.lastrowid

def main():
    database = "database1.db"
 
    sql_crear_tabla_mediciones = """ CREATE TABLE IF NOT EXISTS datos (
                                        id integer PRIMARY KEY,
                                        fecha real,
                                        temperatura text,
                                        humedad text,
                                        presion_atmosferica text,
                                        radiacion_solar text,
                                        velocidad_viento text,
                                        direccion_viento text,
                                        cobertura_nubes text,
                                        precipitacion text,
                                        ozono_troposferico text,
                                        vapor_agua text
                                    ); """
    conn = crear_conexion(database)
    if conn is not None:
        crear_tabla(conn, sql_crear_tabla_mediciones)
    else:
        print("Error! cannot create the database connection.")
    with conn:
        # crear una nueva linea de mediciones
        humi, temp, date_time = DHT11_data()
        mediciones = (date_time,temp,humi,0,0,0,0,0,0,0,0)
        return insertar_datos(conn, mediciones)

if __name__ == '__main__':
    main ()
