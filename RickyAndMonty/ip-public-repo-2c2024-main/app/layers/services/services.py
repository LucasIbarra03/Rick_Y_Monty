# capa de servicio/lógica de negocio

from ..persistence import repositories
from ..utilities import translator
from django.contrib.auth import get_user
import requests 
def getAllImages(input=None):
    url = "https://rickandmortyapi.com/api/character/" # URL de la API de Rick & Morty para obtener personajes

    response = requests.get(url)  # Realizamos la solicitud GET a la API

    if response.status_code == 200: # Verificamos si la solicitud fue exitosa
        data = response.json()  # Convertimos la respuesta en formato JSON

        images = []
        for character in data['results']: # Iteramos sobre la lista de personajes en la respuesta de la API
            episode_url = character['episode'][0] # Obtenemos la URL del primer episodio del personaje
            
            # Realizamos una solicitud adicional para obtener los datos del episodio
            episode_response = requests.get(episode_url)
            episode_data = episode_response.json()
            
            # Obtenemos el nombre del episodio inicial
            episode_name = episode_data['name']  

            # Obtenemos la última ubicación del personaje
            last_location = character['location']['name']

            # Agregamos la informacion del personaje
            character_data = {
                'name': character['name'],  # Nombre del personaje
                'image': character['image'],  # URL de la imagen
                'status': character['status'],  # Estado del personaje (Alive, Dead, etc.)
                'last_location': last_location,  # Última ubicación conocida
                'episode_name': episode_name,  # Nombre del primer episodio donde aparece
            }
            
            # Agregamos el personaje a la lista
            images.append(character_data)

        return images

def deleteFavourite(request):
    favId = request.POST.get('id')
    return repositories.deleteFavourite(favId) # borramos un favorito por su ID.
