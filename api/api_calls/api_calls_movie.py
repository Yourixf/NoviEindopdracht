import requests
import config
import api.api_error_handling as api_error_handling
import api.api_data_handling.api_data_handling_general as api_data_handling_general
import api.api_data_handling.api_data_handling_movie as api_data_handling_movie


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
        "api_key": f"{config.krijg_authorisatie()}",
        "query": f"{gebruiker_film_titel}"
    }

    response = requests.get(API_ENDPOINT_URL, params=payload, headers=headers)

    # Controleert wat de server response code is.
    status_code = api_error_handling.controleer_status_code(response)

    # Als server response code 200 is zal de data worden geformateerd in formateer_film_lijst
    if status_code[0] == 200:
        resulaten_gekregen = api_data_handling_movie.formateer_film_lijst(response, gebruiker_film_titel)
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
        "api_key": f"{config.krijg_authorisatie()}"
    }

    response = requests.get(API_ENDPOINT_URL + gebruiker_film_ID, params=payload, headers=headers)

    # controleert wat de server response code is.
    status_code = api_error_handling.controleer_status_code(response)

    if status_code[0] == 200:
        resulaten_gekregen = api_data_handling_movie.formateer_film_details(response)
    else:
        print(f"{status_code[0]} - {status_code[1]}")
        resulaten_gekregen = False

    # Word geprint als logging variabele in main.py op True staat.
    if config.terminal_logging:
        print(f"Logging - Response code: {status_code[0]} - {status_code[1]}")

    return resulaten_gekregen


def zoek_film_acteur_lijst(gebruiker_acteur_ID=None):
    """
    Deze functie maakt een API request voor een film lijst op basis van een acteur.

    Deze functie krijgt een acteur naam vanuit de aanroepende functie en maakt een API call.
    Daarna controleert de functie de status code, en formateerd de response en retourneert een boolean waarde
    of de response inhoud had vanuit de formateer functie.
    """

    API_ENDPOINT_URL = "https://api.themoviedb.org/3/discover/movie"

    headers = {
        "accept": "application/json",
    }

    payload = {
        "api_key": f"{config.krijg_authorisatie()}",
        "with_cast": f"{gebruiker_acteur_ID}"
    }

    response = requests.get(API_ENDPOINT_URL, params=payload, headers=headers)

    # Controleert wat de server response code is.
    status_code = api_error_handling.controleer_status_code(response)

    # Als server response code 200 is zal de data worden geformateerd in formateer_film_lijst
    if status_code[0] == 200:
        resulaten_gekregen = api_data_handling_movie.formateer_film_lijst(response, gebruiker_acteur_ID)

    else:
        print(f"{status_code[0]} - {status_code[1]}")
        resulaten_gekregen = False

    # Word geprint als logging variabele in config.py op True staat.
    if config.terminal_logging:
        print(f"Logging - Response code: {status_code[0]} - {status_code[1]}")

    return resulaten_gekregen