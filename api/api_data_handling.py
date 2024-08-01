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

        # Word geprint als logging variabele in main.py op True staat.
        if config.terminal_logging:
            print("Logging - Geen film lijst weergegeven")
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
            print("Logging - Film lijst weergegeven")

        return True


def formateer_film_details(response=None):
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
    print("Alle beschikbare informatie over: FILM TITEL \n") # TO DO FIX

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

            # Word geprint als logging variabele in main.py op True staat.
            if config.terminal_logging:
                print("Logging - Film details weergegeven")

            return True
        elif key not in response_dict:
            print("Geen details gevonden.")

            # Word geprint als logging variabele in main.py op True staat.
            if config.terminal_logging:
                print("Logging - Geen film details weergegeven")

            return False


def formateer_acteur_lijst(response=None, gebruiker_acteur_naam=None):
    """
    Deze functie formateert de actuer response lijst.

    Deze functie wordt aangeroepen vanuit api_calls.zoek_acteur_naam() die een response meegeeft
    die vervolgens gecontroleerd wordt op inhoud en formateerd en presenteerd aan de gebruikt.
    Als laatst zal de functie een boolean retourneren aan de aanroepende functie.

    """
    response_dict = response.json()

    if response_dict.get("total_results", 0) == 0:
        print(f"Geen resultaten voor: {gebruiker_acteur_naam}")

        # Word geprint als logging variabele in main.py op True staat.
        if config.terminal_logging:
            print("Logging - Geen acteur lijst weergegeven")

        return False
    else:
        print("-" * 50)
        for movie in response_dict.get("results", []):
            # De Get methode controleert of de waarde niet bestaat, en de strip methode vervangt de niet bestaande
            # met ONBEKEND, en deze waarde wordt via formateer_maximale_grootte gemaximaliseerd
            name = formateer_maximale_grootte(movie.get("name", "").strip() or "ONBEKEND")
            original_name = formateer_maximale_grootte(movie.get("original_name", "").strip() or "ONBEKEND")
            gender = formateer_maximale_grootte(str(movie.get("gender", "")).strip() or "ONBEKEND")
            known_for_department = formateer_maximale_grootte(movie.get("known_for_department").strip() or "ONBEKEND")
            popularity = formateer_maximale_grootte(str(movie.get("popularity", "")).strip() or "ONBEKEND")
            known_for_list = formateer_maximale_grootte(movie.get("known_for", []))
            known_for_movie = formateer_maximale_grootte(str(known_for_list[0].get("original_title")).strip() or "ONBEKEND")
            actor_id = formateer_maximale_grootte(str(movie.get("id", "")).strip() or "ONBEKEND")

            if gender == "1":
                gender = "Vrouw"
            elif gender == "2":
                gender = "Man"
            elif gender == "3":
                gender = "Non binair"

            print(f"Naam: {name}")
            print(f"Oorspronkelijke naam: {original_name}")
            print(f"Geslacht: {gender}")
            print(f"Bekend voor: {known_for_department}")
            print(f"Populariteit score: {popularity}")
            print(f"Bekend van de titel: {known_for_movie}")
            print(f"Acteur ID nummer: {actor_id}")
            print("-" * 50)

        # Word geprint als logging variabele in main.py op True staat.
        if config.terminal_logging:
            print("Logging - Acteur lijst weergegeven")

        return True