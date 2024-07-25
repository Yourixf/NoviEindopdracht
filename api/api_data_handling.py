import json
import config


def formateer_film_lijst(response=None, gebruiker_film_titel=None):
    """
    Deze functie formateert de flm lijst response.

    Deze functie kijkt eerst of er resultaten zijn, en indien er wel resultaten zijn word deze op een duidelijke manier
    weergegeven aan de gebruiker.
    """
    response_dict = response.json()
    formatted_json = json.dumps(response_dict, indent=1)

    if response_dict.get("total_results", 0) == 0:
        print(f"Geen resultaten voor: {gebruiker_film_titel}")
        return False
    else:
        print("-" * 50)
        for movie in response_dict.get("results", []):
            # De Get methode controleert of de waarde niet bestaat, en de strip methode vervangt de niet bestaande met ONBEKEND,
            title = movie.get("title", "").strip() or "ONBEKEND"
            release_date = movie.get("release_date", "").strip() or "ONBEKEND"
            overview = movie.get("overview", "").strip() or "ONBEKEND"
            movie_id = str(movie.get("id", "")).strip() or "ONBEKEND"

            print(f"Titel: {title}")
            print(f"Release Datum: {release_date}")
            print(f"Omschrijving: {overview}")
            print(f"Film ID nummer: {movie_id}")
            print("-" * 50)

        # Word geprint als logging variabele in main.py op True staat.
        if config.terminal_logging:
            print("Logging - Resultaten weergegeven")

        return True


def formateer_film_details(response=None):
    """
    Deze functie formateert de film details response.
    """

    response_dict = response.json()
    formatted_json = json.dumps(response_dict, indent=1)


    film_details_lijst = response_dict[
        "Adult",
        "genres",  #zoek genre nummer
        "origin_country",
        "original_language"
    ]
    print(film_details_lijst)
