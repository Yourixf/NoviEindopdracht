import requests
import config
import user_interface.menu
import api.api_error_handling as api_error_handling
import api.api_data_handling as api_data_handling


def krijg_authorisatie():
    """
    Deze functie word voorziet andere API call functies van authorisatie.

    Deze functie retourneert mijn persoonlijke API Key in de API_KEY_AUTHORISATIE constante variabel
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
        "api_key": f"{krijg_authorisatie()}",
        "query": f"{gebruiker_film_titel}"
    }

    response = requests.get(API_ENDPOINT_URL, params=payload, headers=headers)

    # Controleert wat de server response code is.
    status_code = api_error_handling.controleer_status_code(response)

    # Als server response code 200 is zal de data worden geformateerd in formateer_film_lijst
    if status_code[0] == 200:
        resulaten_gekregen = api_data_handling.formateer_film_lijst(response, gebruiker_film_titel)
    else:
        print(f"{status_code[0]} - {status_code[1]}")
        resulaten_gekregen = False

    keuze_submenu = user_interface.menu.submenu_optie_1(resulaten_gekregen)

    # Word geprint als logging variabele in config.py op True staat.
    if config.terminal_logging:
        print(f"Logging - Response code: {status_code[0]} - {status_code[1]}")

    return keuze_submenu, resulaten_gekregen

def zoek_film_details(gebruiker_film_ID=None):
    """
    Deze functie maakt een API call en zoekt de details van een film

    Deze functie ontvangt een film id vanuit de gebruiker die in de payload van de query word gebruikt
    om de data terug te krijgen die vervolgens geformateerd word.
    """

    API_ENDPOINT_URL = "https://api.themoviedb.org/3/movie/"

    headers = {
        "accept": "application/json",
    }

    payload = {
        "api_key": f"{krijg_authorisatie()}"
    }

    response = requests.get(API_ENDPOINT_URL + gebruiker_film_ID, params=payload, headers=headers)

    # controleert wat de server response code is.
    status_code = api_error_handling.controleer_status_code(response)

    if status_code[0] == 200:
        resulaten_gekregen = api_data_handling.formateer_film_details(response)
    else:
        print(f"{status_code[0]} - {status_code[1]}")
        resulaten_gekregen = False

    # Word geprint als logging variabele in main.py op True staat.
    if config.terminal_logging:
        print(f"Logging - Response code: {status_code[0]} - {status_code[1]}")

    return resulaten_gekregen
