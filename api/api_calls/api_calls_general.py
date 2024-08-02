import requests
import config
import api.api_error_handling as api_error_handling


def test_api():
    #url = "https://api.themoviedb.org/3/search/movie?api_key=73848e07266dcffa72c033c48439c581"
    endpoint_url = "https://api.themoviedb.org/3/discover/movie"

    with_genres = f"Horror"
    url = endpoint_url
    headers = {
        "accept": "application/json",
    }

    payload = {
        "api_key": f"{config.krijg_authorisatie()}",
        "with_genres": f"27"
    }

    response = requests.get(url, params=payload, headers=headers)

    for movie in response:
        print(movie)


def krijg_beschikbare_film_genres():  #overbodig momenteel
    API_ENDPOINT_URL = "https://api.themoviedb.org/3/genre/movie/list"

    genre_taal = "nl"

    headers = {
        "accept": "application/json",
    }

    payload = {
        "api_key": f"{config.krijg_authorisatie()}",
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


