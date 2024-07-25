import requests
import json

import user_interface.menu
import user_interface.user_error_handling as user_error_handling
import api.api_error_handling as api_error_handling

def krijg_authorisatie():
    """
    Deze functie word voorziet andere API call functies van authorisatie.

    Deze functie retourneert mijn persoonlijke API Key in de API_KEY_AUTHORISATIE
    aan de functie die een API endpoint aanroept zodat deze toegang krijgt.
    """

    API_KEY_AUTHORISATIE = "73848e07266dcffa72c033c48439c581"
    return API_KEY_AUTHORISATIE


def test_api():
    #url = "https://api.themoviedb.org/3/search/movie?api_key=73848e07266dcffa72c033c48439c581"
    endpoint_url = "https://api.themoviedb.org/3/search/movie"

    query = f"Iron Man"
    url = endpoint_url
    headers = {
        "accept": "application/json",
    }

    payload = {
        "api_key": f"{krijg_authorisatie()}",
        "query": f"{query}"
    }

    response = requests.get(url, params=payload, headers=headers)

    for movie in response:
        print(movie[7])

def zoek_film_naam(gebruiker_film_titel=None):
    """
    Deze functie maakt een API call en zoekt naar films

    Deze functie ontvangt gebruikers input vanuit menu.hoofdmenu_optie_1 en
    gebruikt deze in de payload om te zoeken
    """

    API_ENDPOINT_URL = "https://api.themoviedb.org/3/search/movie"

    headers = {
        "accept": "application/json",
    }

    payload = {
        "api_key" : f"{krijg_authorisatie()}",
        "query" : f"{gebruiker_film_titel}"
    }
    response = requests.get(API_ENDPOINT_URL, params=payload, headers=headers)

    status_code = api_error_handling.controleer_status_code(response)

    print(f"Response code: {status_code[0]} - {status_code[1]}")

    if status_code[0] == 200:
        response_dict = response.json()
        formatted_json = json.dumps(response_dict, indent=1)

        print(formatted_json)

        for movie in response_dict["results"]:
            title = movie["title"]
            release_date = movie["release_date"]
            overview = movie["overview"]
            movie_id = movie["id"]

            print(f"Titel: {title}")
            print(f"Release Datum: {release_date}")
            print(f"Overzicht: {overview}")
            print(f"Film ID nummer: {movie_id}")
            print("___")


    keuze_submenu = user_interface.menu.submenu_optie_1()

    return status_code[0], keuze_submenu