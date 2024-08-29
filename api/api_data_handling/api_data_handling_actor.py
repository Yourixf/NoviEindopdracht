import config
import api.api_data_handling.api_data_handling_general as api_data_handling_general
from api.api_data_handling.api_data_handling_general import formateer_maximale_grootte

def formateer_acteur_lijst(response=None, gebruiker_acteur_naam=None):
    """
    Deze functie formateert de actuer response lijst.

    Deze functie wordt aangeroepen vanuit api_calls.zoek_acteur_naam() die een response meegeeft
    die vervolgens gecontroleerd wordt op inhoud en formateerd en presenteerd aan de gebruikt.
    Als laatst zal de functie een boolean retourneren aan de aanroepende functie.

    """
    response_dict = response.json()

    if response_dict.get("total_results", 0) == 0:
        print(f"Geen resultaten voor: {gebruiker_acteur_naam}\n")

        # Word geprint als logging variabele in main.py op True staat.
        if config.terminal_logging:
            print("Logging - Geen acteur lijst weergegeven")

        return False, response
    else:
        print("-" * 50)
        for acteur in response_dict.get("results", []):
            # De Get methode controleert of de waarde niet bestaat, en de strip methode vervangt de niet bestaande
            # met ONBEKEND, en deze waarde wordt via formateer_maximale_grootte gemaximaliseerd
            name = formateer_maximale_grootte(acteur.get("name", "").strip() or "ONBEKEND")
            original_name = formateer_maximale_grootte(acteur.get("original_name", "").strip() or "ONBEKEND")
            gender = formateer_maximale_grootte(str(acteur.get("gender", "")).strip() or "ONBEKEND")
            known_for_department_list = formateer_maximale_grootte(acteur.get("known_for_department", []))
            known_for_department = formateer_maximale_grootte(acteur.get("known_for_department", "").strip()
                                                              or "ONBEKEND")
            popularity = formateer_maximale_grootte(str(acteur.get("popularity", "")).strip() or "ONBEKEND")
            known_for_list = formateer_maximale_grootte(acteur.get("known_for", []))
            known_for_movie = formateer_maximale_grootte(known_for_list[0].get("original_title", "ONBEKEND")
                                                         if known_for_list else "ONBEKEND")
            actor_id = formateer_maximale_grootte(str(acteur.get("id", "")).strip() or "ONBEKEND")

            if gender == "0":
                gender = "ONBEKEND"
            elif gender == "1":
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

        return True, response


def formateer_acteur_details(response=None, gebruiker_acteur_id=None):
    response_dict = response.json()

    film_details_volgorde_tuple = (
        "name",
        "gender",
        "birthday",
        "deathday",
        "place_of_birth",
        "adult",
        "also_known_as",
        "known_for_department",
        "popularity",
        "biography",
        "id"
    )

    key_map_dict = {
        "adult": "Voor volwassenen",
        "also_known_as": "Bekend als",
        "id": "ID",
        "biography": "Biographie",
        "birthday": "Geboortedatum",
        "deathday": "Sterfdag",
        "gender": "Geslacht",
        "known_for_department": "Bekend voor",
        "name": "Naam",
        "place_of_birth": "Geboorteplaats",
        "popularity": "Populariteit"
    }

    print("-" * 50)
    print(f"Alle beschikbare informatie over: {gebruiker_acteur_id}\n")

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

                if key == "gender":
                    if value == "0":
                        value = "Onbekend"
                    elif value == "1":
                        value = "Vrouw"
                    elif value == "2":
                        value = "Man"
                    elif value == "3":
                        value = "Non binair"
            else:
                value = value.strip() if isinstance(value, str) else value

            if not value:
                value = "ONBEKEND"

            # Zorgt ervoor dat de geprinte waardes niet breder is dan 50 characters.
            geformateerde_value = api_data_handling_general.formateer_maximale_grootte(value, max_length=50)

            print(f"{key_map_dict.get(key, key.capitalize())}: {geformateerde_value}")

        elif key not in response_dict:
            print("-" * 50)
            print("Geen details gevonden.")

    print("-" * 50)

    if key not in response_dict:
        # Word geprint als logging variabele in main.py op True staat.
        if config.terminal_logging:
            print("Logging - Geen acteur details weergegeven")
        return False
    elif key in response_dict:
        # Word geprint als logging variabele in main.py op True staat.
        if config.terminal_logging:
            print("Logging - Acteur details weergegeven")
        return True

def formateer_geslacht_acteur_lijst(response=None, gebruiker_acteur_geslacht=None):
    """
    Deze functie formateert de geslacht acteur lijst.

    Deze functie wordt aangeropen vanuit helper_methods_general.py filter_acteur_geslacht().
    De functie zal over de data itereren, formateren en presenteren aan de gebruiker
    als het gekozen geslacht in de response voorkomt. Tot slot zal deze een boleon waarde
    retourneren aan de aanroepende functie

    """

    response_dict = response.json()
    resultaat_gevonden = False

    if response_dict.get("total_results", 0) == 0:
        print(f"Geen acteur(s) gevonde met jouw  gekozen geslacht\n")

        # Word geprint als logging variabele in main.py op True staat.
        if config.terminal_logging:
            print("Logging - Geen acteur lijst weergegeven\n")

        return False
    else:
        print("-" * 50)
        for acteur in response_dict.get("results", []):
            # De Get methode controleert of de waarde niet bestaat, en de strip methode vervangt de niet bestaande
            # met ONBEKEND, en deze waarde wordt via formater_maximale_grootte gemaximaliseerd
            name = formateer_maximale_grootte(acteur.get("name", "").strip() or "ONBEKEND")
            original_name = formateer_maximale_grootte(acteur.get("original_name", "").strip() or "ONBEKEND")
            gender = formateer_maximale_grootte(str(acteur.get("gender", "")).strip() or "ONBEKEND")
            known_for_department = formateer_maximale_grootte(acteur.get("known_for_department", "").strip() or "ONBEKEND")
            popularity = formateer_maximale_grootte(str(acteur.get("popularity", "")).strip() or "ONBEKEND")
            known_for_list = formateer_maximale_grootte(acteur.get("known_for", []))
            known_for_movie = formateer_maximale_grootte(known_for_list[0].get("original_title", "ONBEKEND")
                                                         if known_for_list else "ONBEKEND")
            actor_id = formateer_maximale_grootte(str(acteur.get("id", "")).strip() or "ONBEKEND")

            if gender == "0":
                geslacht = "Onbekend"
            elif gender == "1":
                geslacht = "Vrouw"
            elif gender == "2":
                geslacht = "Man"
            elif gender == "3":
                geslacht = "Non binair"

            if gender == gebruiker_acteur_geslacht:
                resultaat_gevonden = True
                print(f"Naam: {name}")
                print(f"Oorspronkelijke naam: {original_name}")
                print(f"Geslacht: {geslacht}")
                print(f"Bekend voor: {known_for_department}")
                print(f"Populariteit score: {popularity}")
                print(f"Bekend van de titel: {known_for_movie}")
                print(f"Acteur ID nummer: {actor_id}")
                print("-" * 50)

        if resultaat_gevonden == False:
            print(f"Geen acteur(s) met jou gekozen geslacht.\n")
        elif resultaat_gevonden == True:
            print("Acteur(s) met jouw gekozen geslacht.\n")
        # Word geprint als logging variabele in main.py op True staat.

        if config.terminal_logging and resultaat_gevonden == True:
            print("Logging - Acteur lijst met geslacht weergegeven\n")

        return resultaat_gevonden
