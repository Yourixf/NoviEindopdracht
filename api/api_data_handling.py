import textwrap
import config


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


def formateer_film_lijst(response=None, gebruiker_film_titel=None):
    """
    Deze functie formateert de flm lijst response.

    Deze functie kijkt eerst of er resultaten zijn, en indien er wel resultaten zijn word deze op een duidelijke manier
    weergegeven aan de gebruiker.
    """
    response_dict = response.json()

    if response_dict.get("total_results", 0) == 0:
        print(f"Geen resultaten voor: {gebruiker_film_titel}")
        return False
    else:
        print("-" * 50)
        for movie in response_dict.get("results", []):
            # De Get methode controleert of de waarde niet bestaat, en de strip methode vervangt de niet bestaande
            # met ONBEKEND, en deze waarde wordt via formateer_maximale_grootte gemaximaliseerd
            title = formateer_maximale_grootte(movie.get("title", "").strip() or "ONBEKEND")
            release_date = formateer_maximale_grootte(movie.get("release_date", "").strip() or "ONBEKEND")
            overview = formateer_maximale_grootte(movie.get("overview", "").strip() or "ONBEKEND")
            movie_id = formateer_maximale_grootte(str(movie.get("id", "")).strip() or "ONBEKEND")

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
    print("Alle beschikbare informatie over: FILM TITEL \n")

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
            geformateerde_value = formateer_maximale_grootte(value, max_length=50)

            print(f"{key_map_dict.get(key, key.capitalize())}: {geformateerde_value}")

    return True
