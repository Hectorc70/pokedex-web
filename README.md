<h1> POKEDEX WEB </h1> 

<h2>INSTALACION </h2>
<hr>

<p>Despues de clonar el repositorio.</p><br>
<p>1.- Escriba el siguiente comando para instalar las dependencias</p>

<pre>
 pip install requirements.txt
</pre>

<p>2.- Haga las migraciones de la base de datos, ubicandose en la carpeta raiz del proyecto</p>

<pre>
 python manage.py makemigrations
</pre>
<pre>
 python manage.py migrate
</pre>
 
<p>3.- Posteriormente corra la app</p>

<pre>
 python manage.py runserver
</pre>

<p>3.- En la consola le mostrara la ip y puerto en donde se esta corriendo 
      si ponemos esa ruta en el navegador se verá la aplicación corriendo</p>
 
