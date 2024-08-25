import requests
import config
import api.api_error_handling as api_error_handling
import api.api_data_handling.api_data_handling_actor as api_data_handling_actor


def zoek_acteur_naam(gebruiker_acteur_naam=None):
    """
    Deze functie zoekt een naam van een acteur.

    Deze functie wordt anageroepen vanuit menu.py en krijgt daarvanuit een acteur naam
    waarmee deze een api call maakt, de status daarvan controleerd, de data formateerd en laat zien
    en zal er een boolean vanuit de formateer functie worden geretourneerd aan de aanroepende functie
    """
    API_ENDPOINT_URL = "https://api.themoviedb.org/3/search/person"

    headers = {
        "accept": "application/json",
    }

    payload = {
        "api_key": f"{config.krijg_authorisatie()}",
        "query": f"{gebruiker_acteur_naam}"
    }

    response = requests.get(API_ENDPOINT_URL, params=payload, headers=headers)

    # Controleert wat de server response code is.
    status_code = api_error_handling.controleer_status_code(response)

    # Als server response code 200 is zal de data worden geformateerd in formateer_acteur_lijst

    if status_code[0] == 200:
        resulaten_gekregen = api_data_handling_actor.formateer_acteur_lijst(response, gebruiker_acteur_naam)
    else:
        print(f"{status_code[0]} - {status_code[1]}")
        resulaten_gekregen = False

    # Word geprint als logging variabele in config.py op True staat.
    if config.terminal_logging:
        print(f"Logging - Response code: {status_code[0]} - {status_code[1]}\n")

    return resulaten_gekregen


def zoek_acteur_details(gebruiker_acteur_id=None):
    """
    Deze functie zoekt een weergeeft de details van een actuer.

    Deze functie krijgt vanuit de aanroepende functie een acteur ID, deze wordt meegegven in
    de api call, de status daarvan controleerd, de data formateerd en laat zien
    en zal er een boolean vanuit de formateer functie worden geretourneerd aan de aanroepende functie

    """
    API_ENDPOINT_URL = "https://api.themoviedb.org/3/person/"

    headers = {
        "accept": "application/json",
    }

    payload = {
        "api_key": f"{config.krijg_authorisatie()}"
    }

    response = requests.get(API_ENDPOINT_URL + gebruiker_acteur_id, params=payload, headers=headers)

    # controleert wat de server response code is.
    status_code = api_error_handling.controleer_status_code(response)

    if status_code[0] == 200:
        resulaten_gekregen = api_data_handling_actor.formateer_acteur_details(response, gebruiker_acteur_id)
    else:
        print(f"{status_code[0]} - {status_code[1]}")
        resulaten_gekregen = False

    # Word geprint als logging variabele in main.py op True staat.
    if config.terminal_logging:
        print(f"Logging - Response code: {status_code[0]} - {status_code[1]}\n")

    return resulaten_gekregen
