"""pokedex_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from pokedex import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.view_pokemons, name='index'),
    path('login/', views.ingresar, name='login'),
    path('salir/', views.salir, name='salir'),
    path('registro/', views.registro_usuario, name='registro'),
    path('pokemon-agregar/', views.registro_pokemon, name='pokemon'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
