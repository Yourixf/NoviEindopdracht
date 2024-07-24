import requests

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

    print(response.text)

