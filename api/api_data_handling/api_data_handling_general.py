import config
import textwrap


def formateer_maximale_grootte(value=None, max_length=50):
    """
    Deze functie zorgt ervoor dat de text grootte gemaximaliseerd is.

    Deze functie word aangeroepen vanuit andere functie die iets printen, en geven de
    print waarde een een max lengte, indien geen lente word geleverd is deze standaard 50
    en de waarde word geformateerd en geretouneerd.
    """
    if isinstance(value, str) and len(value) > max_length:
        return '\n'.join(textwrap.wrap(value, width=max_length))
    return value


def formateer_genre_lijst(response=None):
    """
    Deze functie formateert de genre lijst, gerkegen vanuit de API server.

    Deze functie wordt aangeroepen vanuit api_calls_general.py krijg_beschikbare_film_genres().
    Dan zal de functie over de data itereren, vervolgens formateren en presenteren aan de gebruiker.
    Tot slot zal deze een boolean waarde en genre lijst retourneren aan de aanroepende functie.
    """

    response_dict = response.json()
    genre_dict = {}

    if response_dict.get("genres", 0) == 0:
        print("Geen genres vanaf de server gekregen.\n")
        # Word geprint als logging variabele in main.py op True staat.
        if config.terminal_logging:
            print("\nLogging - Geen genres lijst weergegeven\n")
        return False
    else:
        print("-" * 50)
        print("Alle beschikbare genres vanuit de API server:\n")
        for genre in response_dict.get("genres", []):
            # De Get methode controleert of de waarde niet bestaat, en de strip methode vervangt de niet bestaande
            # met ONBEKEND, en deze waarde wordt via formateer_maximale_grootte gemaximaliseerd
            genre_id = formateer_maximale_grootte(str(genre.get("id", "")).strip() or "ONBEKEND")
            genre_name = formateer_maximale_grootte(str(genre.get("name", "")).strip() or "ONBEKEND")

            print(f"ID: {genre_id}, {genre_name}")
            genre_dict.setdefault(genre_id, genre_name)

        print("-" * 50, "\n")

        # Word geprint als logging variabele in main.py op True staat.
        if config.terminal_logging:
            print("\nLogging - Genre lijst weergegeven\n")

        return True, genre_dict


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
            print(f"Geen film(s)  met jou gekozen genre.\n")
        elif resultaat_gevonden == True:
            print("Film(s) met jouw gekozen genre.\n")
        # Word geprint als logging variabele in main.py op True staat.

        if config.terminal_logging and resultaat_gevonden == True:
            print("Logging - Film lijst met genre weergegeven\n")

        return resultaat_gevonden, response


def formateer_release_datum_film_lijst(response=None, gebruiker_release_datum=None):
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
