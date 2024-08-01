import requests
import config
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
    endpoint_url = "https://api.themoviedb.org/3/discover/movie"

    with_genres = f"Horror"
    url = endpoint_url
    headers = {
        "accept": "application/json",
    }

    payload = {
        "api_key": f"{krijg_authorisatie()}",

        "with_genres": f"27"
    }

    response = requests.get(url, params=payload, headers=headers)

    for movie in response:
        print(movie)


def zoek_film_naam(gebruiker_film_titel=None):
    """
    Deze functie maakt een API call en zoekt naar films

    Deze functie ontvangt gebruikers input vanuit menu.hoofdmenu_optie_1 en gebruikt deze
    in de payload om te zoeken en formateerd de response in api_data_handling.formateer_film_lijst.
    Daana zal de functie een boolean, resultaten_gekregen retourneren.
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

    resulaten_gekregen = None

    # Als server response code 200 is zal de data worden geformateerd in formateer_film_lijst
    if status_code[0] == 200:
        resulaten_gekregen = api_data_handling.formateer_film_lijst(response, gebruiker_film_titel)
    else:
        print(f"{status_code[0]} - {status_code[1]}")
        resulaten_gekregen = False

    # Word geprint als logging variabele in config.py op True staat.
    if config.terminal_logging:
        print(f"Logging - Response code: {status_code[0]} - {status_code[1]}")

    return resulaten_gekregen


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

    resulaten_gekregen = None

    if status_code[0] == 200:
        resulaten_gekregen = api_data_handling.formateer_film_details(response)
    else:
        print(f"{status_code[0]} - {status_code[1]}")
        resulaten_gekregen = False

    # Word geprint als logging variabele in main.py op True staat.
    if config.terminal_logging:
        print(f"Logging - Response code: {status_code[0]} - {status_code[1]}")

    return resulaten_gekregen


def krijg_beschikbare_film_genres():  #overbodig momenteel
    API_ENDPOINT_URL = "https://api.themoviedb.org/3/genre/movie/list"

    genre_taal = "nl"

    headers = {
        "accept": "application/json",
    }

    payload = {
        "api_key": f"{krijg_authorisatie()}",
        "language": f"{genre_taal}"
    }

    response = requests.get(API_ENDPOINT_URL, params=payload, headers=headers)

    # controleert wat de server response code is.
    status_code = api_error_handling.controleer_status_code(response)

    if status_code[0] == 200:
        print("Ja jonguh goed gegaan")
        #resulaten_gekregen = api_data_handling.formateer_film_details(response)
    else:
        print(f"{status_code[0]} - {status_code[1]}")
        #resulaten_gekregen = False

    # Word geprint als logging variabele in main.py op True staat.
    if config.terminal_logging:
        print(f"Logging - Response code: {status_code[0]} - {status_code[1]}")

    response_dict = response.json()
    for movie in response_dict.get("genres", []):
        print(movie)

    # make data handling function


def zoek_acteur_naam(gebruiker_acteur_naam=None):
    """
    Deze functie zoekt een naam van een actuer.

    Deze functie wordt anageroepen vanuit menu.py en krijgt daarvanuit een acteur naam
    waarmee deze een api call maakt, de status daarvan controleerd, de data formateerd en laat zien
    en zal er een boolean vanuit de formateer functie worden geretourneerd aan de aanroepende functie
    """
    API_ENDPOINT_URL = "https://api.themoviedb.org/3/search/person"

    headers = {
        "accept": "application/json",
    }

    payload = {
        "api_key": f"{krijg_authorisatie()}",
        "query": f"{gebruiker_acteur_naam}"
    }

    response = requests.get(API_ENDPOINT_URL, params=payload, headers=headers)

    # Controleert wat de server response code is.
    status_code = api_error_handling.controleer_status_code(response)

    # Als server response code 200 is zal de data worden geformateerd in formateer_acteur_lijst
    resulaten_gekregen = None

    if status_code[0] == 200:

        resulaten_gekregen = api_data_handling.formateer_acteur_lijst(response, gebruiker_acteur_naam)
    else:
        print(f"{status_code[0]} - {status_code[1]}")
        resulaten_gekregen = False

    # Word geprint als logging variabele in config.py op True staat.
    if config.terminal_logging:
        print(f"Logging - Response code: {status_code[0]} - {status_code[1]}")

    return resulaten_gekregen
