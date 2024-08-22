import config
import textwrap


def formateer_maximale_grootte(value=None, max_length=50):
    """
    Deze functie zorgt ervoor dat de text grootte gemaximaliseerd is.

    Deze functie word aangeroepen vanuit andere functie die iets printen, en geven de
    print waarde me en een max lengte, indien geen lente word geleverd is deze standaard 50
    en de waarde word geformateerd en geretouneerd.
    """
    if isinstance(value, str) and len(value) > max_length:
        return '\n'.join(textwrap.wrap(value, width=max_length))
    return value


def formateer_genre_lijst(response=None):
    response_dict = response.json()
    genre_dict = {}

    if response_dict.get("genres", 0) == 0:
        # Word geprint als logging variabele in main.py op True staat.
        if config.terminal_logging:
            print("Logging - Geen genres lijst weergegeven")
        return False
    else:
        print("-" * 50)
        print("Alle beschikbare genres vanuit de API server:")
        for genre in response_dict.get("genres", []):
            # De Get methode controleert of de waarde niet bestaat, en de strip methode vervangt de niet bestaande
            # met ONBEKEND, en deze waarde wordt via formateer_maximale_grootte gemaximaliseerd
            genre_id = formateer_maximale_grootte(str(genre.get("id", "")).strip() or "ONBEKEND")
            genre_name = formateer_maximale_grootte(str(genre.get("name", "")).strip() or "ONBEKEND")

            print(f"ID: {genre_id}, {genre_name}")
            genre_dict.setdefault(genre_id, genre_name)
        # Word geprint als logging variabele in main.py op True staat.
        if config.terminal_logging:
            print("Logging - Genre lijst weergegeven")

        return True, genre_dict

def formateer_genre_film_lijst(response=None, gebruiker_genre_id=None):
    response_dict = response.json()
    resultaat_gevonden = None

    if response_dict.get("total_results", 0) == 0:
        print(f"Geen resultaten")
        # Word geprint als logging variabele in main.py op True staat.
        if config.terminal_logging:
            print("Logging - Geen film lijst met genre weergegeven")
        return False
    else:

        print("-" * 50)
        for movie in response_dict.get("results", []):
            # De Get methode controleert of de waarde niet bestaat, en de strip methode vervangt de niet bestaande
            # met ONBEKEND, en deze waarde wordt via formater_maximale_grootte gemaximaliseerd
            title = formateer_maximale_grootte(movie.get("title", "").strip() or "ONBEKEND")
            release_date = formateer_maximale_grootte(
                movie.get("release_date", "").strip() or "ONBEKEND")
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

            # Word geprint als logging variabele in main.py op True staat.
        if config.terminal_logging and resultaat_gevonden == True:
            print("Logging - Film lijst met genre weergegeven")

    return True, response

