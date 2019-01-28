# Templates
 
Para utilizar una plantilla lo primero es crearla, y para ello debemos hacerlo siguiendo una lógica. 
Lo primero es crear un directorio **templates** en nuestra app, que dentro debe contener otro 
directorio con el mismo nombre que la app, en nuestro caso **naranuser**.

Tenemos que hacerlo así porque Django funciona mezclando los directorios templates de las apps, de manera que al 
final él tiene un solo directorio templates y dentro otro para cada app.

Dentro de este subdirectorio **templates/narangram** de la app vamos a comenzar creando un fichero **home.html**:

![crear directorio tempalte](imgs/template1.png "crear directorio tempalte")

Vamos a realizar una primera versión (en crudo, sin estilos) de lo que sería nuestra home en html:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Narangram Home</title>
</head>
<body>
<h1>Mi Web Personal</h1>

<ul>
    <li><a href="/naranuser/">Portada</a></li>
    <li><a href="/login/">Login</a></li>
    <li><a href="/signup/">Signup</a></li>
</ul>

<h2>Bienvenidos</h2>

<p>Esto es la portada de Narangram</p>
</body>
</html>

```

Lo que nos interesa es cambiar nuestra vista para que en lugar de devolver la respuesta HttpResponse devuelva este 
template HTML, y para ello vamos utilizar el método render del módulo http de Django, que ya viene incluido por defecto.

Vamos al fichero **views.py** y realizemos un refactor de nuestra vista hello_world para adaptarla al proyecto:

```
def home(request):
    return render(request, "narangram/home.html")
    
```

Además tenemos que cambiar el nombre de la función en **urls.py** de nuestra aplicación:

```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

```

Una vez hecho vamos a probar si carga la portada, pero como podréis observar no funcionará ya que por defecto Django 
optimiza el uso de la memoria así que no carga las plantillas de una app que no esté instalada en 
settings.py. Para cargar la app core y sus plantillas en memoria debemos ir al fichero **narangram/settings.py** y 
añadir la app en la lista **INSTALLED_APPS** justo abajo del todo:

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'naranuser.apps.NaranuserConfig',
]
```

Ahora probamos de nuevo y... FUNCIONA!

