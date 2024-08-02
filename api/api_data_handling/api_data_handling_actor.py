import config
import api.api_data_handling.api_data_handling_general as api_data_handling_general

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
            name = api_data_handling_general.formateer_maximale_grootte(movie.get("name", "").strip() or "ONBEKEND")
            original_name = api_data_handling_general.formateer_maximale_grootte(movie.get("original_name", "").strip() or "ONBEKEND")
            gender = api_data_handling_general.formateer_maximale_grootte(str(movie.get("gender", "")).strip() or "ONBEKEND")
            known_for_department = api_data_handling_general.formateer_maximale_grootte(movie.get("known_for_department").strip() or "ONBEKEND")
            popularity = api_data_handling_general.formateer_maximale_grootte(str(movie.get("popularity", "")).strip() or "ONBEKEND")
            known_for_list = api_data_handling_general.formateer_maximale_grootte(movie.get("known_for", []))
            known_for_movie = api_data_handling_general.formateer_maximale_grootte(str(known_for_list[0].get("original_title")).strip() or "ONBEKEND")
            actor_id = api_data_handling_general.formateer_maximale_grootte(str(movie.get("id", "")).strip() or "ONBEKEND")

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