from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, permission_required


from .forms import RegistroForm, PokemonForm

from .models import Pokemon


from .services import get_pokemons




# Create your views here.

def verifica_cookie(request):
    if request.session.test_cookie_worked():
        request.session.delate_test_cookie()
    
    else:
        request.session.set_test_cookie()
        messages.error(request, 'Porfavor habilite las cookies')

    return render(request, 'login.html') 
    
def registro_usuario(request):
    formulario = RegistroForm(request.POST or None)

    if request.method == 'POST' and formulario.is_valid():
        name = formulario.cleaned_data.get('username')
        email = formulario.cleaned_data.get('email')
        password = formulario.cleaned_data.get('password')

        
        usuario_r = User.objects.create_user(username=name,  email=email,
                                            password=password,                                 )
        if usuario_r:
            login(request, usuario_r)
            messages.success(request, 'Usuario creado correctamente')

            return redirect('index')

    return render(request, 'register.html', {'form': formulario})

@csrf_protect
def ingresar(request):  
    """vista para poder ingresar a la pagina""" 

    if request.method == 'POST': 
        username = request.POST.get('username')
        psword  = request.POST.get('psword')

        usuario = authenticate(username = username, password = psword)
        if usuario:
            login(request, usuario)

            messages.success(request, 'A ingresado correctamente')
            return redirect('index')
            
        
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return render(request, 'login.html')

    return render(request, 'login.html')

def salir(request):
    logout(request)
    messages.success(request, "Sesion Finalizada")

    return redirect('login') 



def view_pokemons(request):

    pok = Pokemon.objects.all()
    if pok:
        return render(request, 'index.html', {'pokemons':pok})
    else:        
        pokemons = get_pokemons()

        for pokemon, url in pokemons.items():
            poke= Pokemon(name=pokemon, path_sprite=url)
            
            poke.save()


    return render(request, 'index.html', {'pokemons':pok})






def registro_pokemon(request):
    formulario = PokemonForm(request.POST)

    if request.method == 'POST' and formulario.is_valid():

        name = formulario.cleaned_data.get('name')
        path = formulario.cleaned_data.get('path_sprite')

        Pok = Pokemon(name, path)
        Pok.save()

        return redirect('index')

    return render(request, 'pokemon_add.html', {'form': formulario})