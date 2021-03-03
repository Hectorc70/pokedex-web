import requests
import json

import pdb 


BASE_URL = 'https://pokeapi.co'

def query_pokeapi(url):
    url = BASE_URL + url
    response  = requests.get(url)


    if response.status_code == 200:      
        return json.loads(response.text)

    return None




def get_pokemons(params={}):
    ruta_pokemons = '/api/v2/pokemon/'
    data_pokemons = dict()
    pokemons = query_pokeapi(ruta_pokemons)


    for pokemon in pokemons['results']:
        datos = list()
        

        name = pokemon['name']

        #pokemon_id = int(pokemon['url'].split('/')[-1])
        pokemon_url= query_pokeapi(ruta_pokemons + '/' + name)


        sprite_img =  pokemon_url['sprites']['front_default']
        tipos = pokemon_url['types']
        
        datos.append(sprite_img)
        
        data_pokemons[name] = sprite_img

        datos.clear() 

    print(str(data_pokemons))

    return data_pokemons


    