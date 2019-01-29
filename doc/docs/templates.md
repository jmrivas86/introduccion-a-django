# Templates
 
Para utilizar una plantilla lo primero es crearla, y para ello debemos hacerlo siguiendo una lógica. 
Lo primero es crear un directorio **templates** en nuestra app, que dentro debe contener otro 
directorio con el mismo nombre que la app, en nuestro caso **naranuser**.

Tenemos que hacerlo así porque Django funciona mezclando los directorios templates de las apps, de manera que al 
final él tiene un solo directorio templates y dentro otro para cada app.

Dentro de este subdirectorio **templates/narangram** de la app vamos a comenzar creando un fichero **home.html**:

![crear directorio tempalte](imgs/template1.png "crear directorio tempalte")

Vamos a realizar una primera versión (en crudo, sin estilos) de lo que sería nuestra home en html:

```html
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

```python
def home(request):
    return render(request, "narangram/home.html")
    
```

Además tenemos que cambiar el nombre de la función en **urls.py** de nuestra aplicación:

```python
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

```python
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

Ahora probamos de nuevo y... FUNCIONA! pero vamos a darle algo de estilo a nuestro html, añadamos 
[bootstrap](https://getbootstrap.com/docs/4.2/getting-started/download/). Vamos a introducir además el header y 
el footer de la web.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Narangram Home</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
</head>
<body>

<header>
  <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm">
  <h5 class="my-0 mr-md-auto font-weight-normal">Narangram</h5>
  <nav class="my-2 my-md-0 mr-md-3">
    <a class="p-2 text-dark" href="/naranuser/">Portada</a>
  </nav>
  <a class="btn btn-outline-primary" href="#">Sign up</a>
</div>
</header>
<main role="main">

  <section class="jumbotron text-center">
    <div class="container">
      <h1 class="jumbotron-heading">Narangram HOME</h1>
      <p class="lead text-muted">
          Esta es la Home de Narangram
      </p>
    </div>
  </section>

</main>
<footer class="text-muted">
  <div class="container">
    <p class="float-right">
      <a href="#">Back to top</a>
    </p>
    <p>Este es el footer</p>
  </div>
</footer>
</body>
</html>
```

## Herencia de plantillas

Si ahora quisiéramos crear una nueva url para dar información sobre la web, imagina que la llamamos "about", 
¿cómo lo haríamos?...

Iríamos al fichero **views.py** y crearíamos un nuevo método **about**:

```python
def about(request):
    return render(request, "narangram/about.html")
    
```

Además tenemos que añadir esta nueva view en **urls.py** de nuestra aplicación:

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.about, name='about'),
]

```

¿Y el html? ¿qué hacemos con el html?, quiero que antes de responder pienses en una frase:

> En programación, si estás repitiendo código, es que lo estás haciendo mal.

Vale imagina que hacemos "el camino fácil", copiamos el anterior html y añadimos lo que queremos en nuestra nueva vista:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Narangram Home</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
</head>
<body>

<header>
  <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm">
  <h5 class="my-0 mr-md-auto font-weight-normal">Narangram</h5>
  <nav class="my-2 my-md-0 mr-md-3">
    <a class="p-2 text-dark" href="/naranuser/">Portada</a>
  </nav>
  <a class="btn btn-outline-primary" href="#">Sign up</a>
</div>
</header>
<main role="main">

  <section class="jumbotron text-center">
    <div class="container">
      <h1 class="jumbotron-heading">Narangram About</h1>
      <p class="lead text-muted">
          Esta es la sección About de Narangram
      </p>
    </div>
  </section>

</main>
<footer class="text-muted">
  <div class="container">
    <p class="float-right">
      <a href="#">Back to top</a>
    </p>
    <p>Este es el footer</p>
  </div>
</footer>
</body>
</html>
```

Si nos fijamos, el header y el footer será el mismo en las dos vistas. 
Ahora imaginad que queremos cambiar el menú y añadir una nueva sección. ¿Qué problema tendríamos? Pues que deberíamos 
ir una a una cambiando exactamente lo mismo. ¿Es eso ideal? Para nada, más bien es un lastre, y por eso Django nos 
proporciona un sistema muy potente de herencia para nuestras plantillas.

Empezemos de 0, vamos a crear una plantilla base, y en esta ocasión vamos a hacerlo bien. Creamos el fichero base.html 
dentro de templates/naranuser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Narangram Home</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
</head>
<body>

<header>
  <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm">
  <h5 class="my-0 mr-md-auto font-weight-normal">Narangram</h5>
  <nav class="my-2 my-md-0 mr-md-3">
    <a class="p-2 text-dark" href="/naranuser/">Portada</a>
  </nav>
  <a class="btn btn-outline-primary" href="#">Sign up</a>
</div>
</header>
<main role="main">

    {% block content %}{% endblock %}

</main>
<footer class="text-muted">
  <div class="container">
    <p class="float-right">
      <a href="#">Back to top</a>
    </p>
    <p>Este es el footer</p>
  </div>
</footer>
</body>
</html>
```

Podemos ver como hemos añadido la parte repetitiva (header y footer) y hemos añadido una linea 
`{% block content %}{% endblock %}` que es un **template tag** y sirve para añadir lógica de programación dentro del 
propio HTML. Existen muchos template tags en Django, iremos descubriendo algunos de ellos sobre la marcha.

En este caso el template tag **block** sirve para definir un bloque de contenido con un nombre.

Ahora viene la magia, vamos de vuelta por ejemplo a nuestro template home.html y vamos a dejar únicamente la parte de 
código específica de esa plantilla:

```html
{% extends 'naranuser/base.html' %}

{% block content %}
<section class="jumbotron text-center">
    <div class="container">
        <h1 class="jumbotron-heading">Narangram About</h1>
        <p class="lead text-muted">
            Esta es la sección About de Narangram
        </p>
    </div>
</section>
{% endblock %}

```

Podemos ver como hemos utilizado el template tag `extends` para indicarle a la plantilla **home.html** que herede el 
contenido de **base.html** y como hemos marcado con el template tag `block` el contenido que es propio de la sección
home.

## Ejercicio

Adapta el código en **base.html**, **home.html** y **about.html** para que el **title** de la página sea también propio
de cada sección.

## Template tags