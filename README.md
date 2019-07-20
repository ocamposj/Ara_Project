# Django TODO template

### Cosas que no vamos a ver aca pero que estaria bueno que investiguen

* Configurar bases de datos
* instalar y correr todo en un `virtualenv`
* deployment correcto con un servidor
* Correcto manejo de URLs entre distintas apps

### Pasos que se siguieron para llegar a este punto
* En la terminal:
```bash
pip3 install django==2.2 #instalamos django con pip(manejador de paquetes de python)
django-admin startproject Set_up #creamos el proyecto todolist
cd Set_up #entramos al directorio
python3 manage.py startapp Ara_project_web #se crea la app pendientes(un proyecto puede tener muchas apps)
#Set_up/settings.py -> agregar 'Ara_project_web' a installed apps
#Ara_project_web/models.py -> Crear modelo/tabla Datos
#Ara_project_web/models.py -> Registar modelo Datos en la interfaz de Administracion
python3 manage.py makemigrations #se crea el archivo de migracion de base de datos
python3 manage.py migrate #guardamos los cambios en la base de datos(archivo db.sqlite3)
python3 manage.py createsuperuser #se crea un usuario administrador, en este caso admin:admin

python3 manage.py runserver #corremos el servidor de desarrollo
# Abrir el navegador en http:localhost:8000
# http:localhost:8000/admin para la interfaz de administracion
```

* en `Set_up/settings.py`:
  * se agrega `'Ara_project_view'` a `INSTALLED_APPS`
  * se cambia el idioma a español

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Ara_project_web' #esta linea es la que agregamos
]
```
```python
LANGUAGE_CODE = 'es'
``` 

* en `Ara_project_web/models.py` creamos el modelo Tarea (modelo ~= tabla de la base de datos)

```python
class Datos(models.Model):
    titulo = models.CharField(max_length=100) #Campo/columna titulo de tipo "campo de caracteres" de longitud maxima de 100
    descripcion = models.TextField(null=True, blank=True) #Campo/columna titulo de tipo Texto, los argumentos blank y null son para que el campo sea opcional
    estado = models.BooleanField(default=False)
```

* en `Ara_project_web/admin.py` registramos nuestro modelo para poder usarlo en la interfaz de administracion

```python
from django.contrib import admin
from .models import Datos #importamos el modelo

admin.site.register(Datos) #lo registramos

```

* en `Ara_project_web/views.py`

```python
from django.http import HttpResponse

def index(request):
    saludo = "Hola, Mundo! Esta es la raiz /"
    return HttpResponse(saludo) #retornamos el saludo
```

* en `Set_up/urls.py`

```python
from Ara_project_web import views #importamos las vistas de la app/directorio pendientes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), #Creamos la ruta raiz '' y la enlazamos con nuestra vista index del archivo views.py
]

```


