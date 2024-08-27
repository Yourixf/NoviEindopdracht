import config
import api.api_data_handling.api_data_handling_general as api_data_handling_general
from api.api_data_handling.api_data_handling_general import formateer_maximale_grootte


def formateer_film_lijst(response=None, gebruiker_film_titel=None):
    """
    Deze functie formateert de flm lijst response.

    Deze functie kijkt eerst of er resultaten zijn, en indien er wel resultaten zijn word deze op een duidelijke
    manier weergegeven aan de gebruiker.
    """
    response_dict = response.json()

    if response_dict.get("total_results", 0) == 0:
        print(f"Geen resultaten voor: {gebruiker_film_titel}\n")

        # Word geprint als logging variabele in main.py op True staat.
        if config.terminal_logging:
            print("Logging - Geen film lijst weergegeven\n")
        return False, response
    else:
        print("-" * 50)
        for movie in response_dict.get("results", []):
            # De Get methode controleert of de waarde niet bestaat, en de strip methode vervangt de niet bestaande
            # met ONBEKEND, en deze waarde wordt via formateer_maximale_grootte gemaximaliseerd
            title = api_data_handling_general.formateer_maximale_grootte(movie.get("title", "").strip() or "ONBEKEND")
            release_date = api_data_handling_general.formateer_maximale_grootte(movie.get("release_date", "").strip() or "ONBEKEND")
            overview = api_data_handling_general.formateer_maximale_grootte(movie.get("overview", "").strip() or "ONBEKEND")
            movie_id = api_data_handling_general.formateer_maximale_grootte(str(movie.get("id", "")).strip() or "ONBEKEND")

            print(f"Titel: {title}")
            print(f"Release Datum: {release_date}")
            print(f"Omschrijving: {overview}")
            print(f"Film ID nummer: {movie_id}")
            print("-" * 50)

        # Word geprint als logging variabele in main.py op True staat.
        if config.terminal_logging:
            print("Logging - Film lijst weergegeven")

        return True, response


def formateer_film_details(response=None, gebruiker_film_ID=None):
    """
    Deze functie formateert de film details response.

    Deze functie krijgt een API response van een film detail call, dan al deze
    functie over de data itereren, vervolgens formateren en presenteren aan de gebruiker.
    Tot slot zal deze een boolean waarde retourneren aan de aanroepende functie.
    """

    response_dict = response.json()

    film_details_volgorde_tuple = (
        "title",
        "original_title",
        "overview",
        "release_date",
        "genres",
        "adult",
        "status",
        "origin_country",
        "original_language",
        "spoken_languages",
        "production_companies",
        "production_countries",
        "id"
    )

    key_map_dict = {
        "adult": "Voor volwassenen",
        "genres": "Genres",
        "id": "ID",
        "origin_country": "Oorsprongsland",
        "original_language": "Originele taal",
        "original_title": "Originele titel",
        "overview": "Omschrijving",
        "production_companies": "Productiebedrijven",
        "production_countries": "Productielanden",
        "release_date": "Releasedatum",
        "spoken_languages": "Gesproken talen",
        "status": "Status",
        "title": "Titel"
    }

    print("-" * 50)
    print(f"Alle beschikbare informatie over: {gebruiker_film_ID}\n")

    # Itereer door response
    for key in film_details_volgorde_tuple:
        # Controleert of item in response zit
        if key in response_dict:
            value = response_dict[key]
            # controlleert of de waarde een bool is
            if isinstance(value, bool):
                # Als waarde True is: Ja, als waarde False is: Nee.
                value = "Ja" if value else "Nee"
            elif isinstance(value, list):
                # Al de respone een sub dict een key name bevat, zal deze erop itereren
                # en de values in 1 string plaatsen
                if all(isinstance(item, dict) and 'name' in item for item in value):
                    value = ", ".join(item['name'] for item in value)
                else:
                    value = ", ".join(str(item) for item in value)
            elif isinstance(value, (int, float)):
                value = str(value)
            else:
                value = value.strip() if isinstance(value, str) else value

            if not value:
                value = "ONBEKEND"

            # Zorgt ervoor dat de geprinte waardes niet breder is dan 50 characters.
            geformateerde_value = api_data_handling_general.formateer_maximale_grootte(value, max_length=50)

            print(f"{key_map_dict.get(key, key.capitalize())}: {geformateerde_value}")

        elif key not in response_dict:
            print("Geen details gevonden.")

    if key not in response_dict:
        # Word geprint als logging variabele in main.py op True staat.
        if config.terminal_logging:
            print("Logging - Geen film details weergegeven\n")
        return False
    elif key in response_dict:
        # Word geprint als logging variabele in main.py op True staat.
        if config.terminal_logging:
            print("\nLogging - Film details weergegeven")
        return True


def formateer_genre_film_lijst(response=None, gebruiker_genre_id=None):
    """
    Deze functie formateert de genre film lijst.

    Deze functie wordt aangeroepen vanuit menu.py filter_genre()
    De functie za; over de data itereren, vervolgens formateren en presenteren aan de gebruiker.
    Tot slot zal deze een boolean waarde en de response retourneren aan de aanroepende functie.
    """
    response_dict = response.json()
    resultaat_gevonden = False

    if response_dict.get("total_results", 0) == 0:
        print(f"Geen film(s) met jou gekozen genre.\n")
        # Word geprint als logging variabele in main.py op True staat.
        if config.terminal_logging:
            print("Logging - Geen film lijst met genre weergegeven\n")
        return False
    else:
        print("-" * 50)
        for movie in response_dict.get("results", []):
            # De Get methode controleert of de waarde niet bestaat, en de strip methode vervangt de niet bestaande
            # met ONBEKEND, en deze waarde wordt via formater_maximale_grootte gemaximaliseerd
            title = formateer_maximale_grootte(movie.get("title", "").strip() or "ONBEKEND")
            release_date = formateer_maximale_grootte(movie.get("release_date", "").strip() or "ONBEKEND")
            overview = formateer_maximale_grootte(movie.get("overview", "").strip() or "ONBEKEND")
            movie_id = formateer_maximale_grootte(str(movie.get("id", "")).strip() or "ONBEKEND")

            genre_ids = formateer_maximale_grootte(str(movie.get("genre_ids", "")).strip() or "ONBEKEND")

            if gebruiker_genre_id in genre_ids:
                resultaat_gevonden = True
                print(f"Titel: {title}")
                print(f"Release Datum: {release_date}")
                print(f"Omschrijving: {overview}")
                print(f"Film ID nummer: {movie_id}")
                print("-" * 50)

        if resultaat_gevonden == False:
            print(f"Geen film(s) met jou gekozen genre.\n")
        elif resultaat_gevonden == True:
            print("Film(s) met jouw gekozen genre.\n")
        # Word geprint als logging variabele in main.py op True staat.

        if config.terminal_logging and resultaat_gevonden == True:
            print("Logging - Film lijst met genre weergegeven\n")

        return resultaat_gevonden, response


def formateer_release_datum_film_lijst(response=None, gebruiker_release_datum=None):
    """
    Deze functie formateert de genre film lijst.

    Deze functie wordt aangeroepen vanuit general_methods filter_genre()
    De functie zal over de data itereren, vervolgens formateren en presenteren aan de gebruiker
    als het gekozen jaartal in de repsonse zit. Tot slot zal deze een boolean waarde en de response
    retourneren aan de aanroepende functie.
    """
    response_dict = response.json()
    resultaat_gevonden = False

    if response_dict.get("total_results", 0) == 0:
        print(f"Geen film(s) met jou gekozen genre.\n")
        # Word geprint als logging variabele in main.py op True staat.
        if config.terminal_logging:
            print("Logging - Geen film lijst met genre weergegeven\n")
        return False
    else:
        print("-" * 50)
        for movie in response_dict.get("results", []):
            # De Get methode controleert of de waarde niet bestaat, en de strip methode vervangt de niet bestaande
            # met ONBEKEND, en deze waarde wordt via formater_maximale_grootte gemaximaliseerd
            title = formateer_maximale_grootte(movie.get("title", "").strip() or "ONBEKEND")
            overview = formateer_maximale_grootte(movie.get("overview", "").strip() or "ONBEKEND")
            movie_id = formateer_maximale_grootte(str(movie.get("id", "")).strip() or "ONBEKEND")
            full_release_date = formateer_maximale_grootte(movie.get("release_date", "").strip() or "ONBEKEND")
            release_date_year =  full_release_date.split("-")[0]

            if gebruiker_release_datum == release_date_year:
                resultaat_gevonden = True
                print(f"Titel: {title}")
                print(f"Release Datum: {full_release_date}")
                print(f"Omschrijving: {overview}")
                print(f"Film ID nummer: {movie_id}")
                print("-" * 50)

        if resultaat_gevonden == False:
            print(f"Geen film(s)  met jou gekozen jaartal.\n")
        elif resultaat_gevonden == True:
            print("Film(s) met jouw gekozen jaartal.\n")
        # Word geprint als logging variabele in main.py op True staat.

        if config.terminal_logging and resultaat_gevonden == True:
            print("Logging - Film lijst met jouw jaartal weergegeven\n")

        return resultaat_gevonden

