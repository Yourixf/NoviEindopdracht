from api.api_calls.api_calls_movie import zoek_film_naam, zoek_film_details, zoek_film_acteur_lijst
from api.api_data_handling.api_data_handling_movie import formateer_release_datum_film_lijst


def krijg_film_lijst():
    """
    nog beschrijven v2
    """
    klaar_met_zoeken = False
    resultaten_gekregen = False, {}

    while not klaar_met_zoeken:
        gebruiker_film_titel = input("Wat is de titel van de film die je wilt opzoeken? (0 om te annuleren): ")

        if gebruiker_film_titel == "0":
            klaar_met_zoeken = True
        elif gebruiker_film_titel == "" or None:
            print("\nOngeldig invoer, voer een titel in.\n")
        else:
            resultaten_gekregen = zoek_film_naam(gebruiker_film_titel)
            if resultaten_gekregen[0] is True:
                klaar_met_zoeken = True

    if klaar_met_zoeken is True:
        return resultaten_gekregen


def krijg_film_details():
    """
    NOG BESCHRIJVEN
    """

    klaar_met_zoeken = False

    while not klaar_met_zoeken:
        gebruiker_film_ID = input("Wat is het ID van de film? (zie lijst, 0 om te annuleren): ")

        if gebruiker_film_ID == "0":
            klaar_met_zoeken = True
        elif gebruiker_film_ID == "" or None:
            print("\nOngeldig invoer, voer een ID in.\n")
        else:
            details_gekregen = zoek_film_details(gebruiker_film_ID)
            if details_gekregen is True:
                klaar_met_zoeken = True


def krijg_film_acteur_lijst():
    """
    nog bescrhijven v2
    """
    klaar_met_zoeken = False

    while not klaar_met_zoeken:
        gebruiker_acteur_ID = input("Wat is het ID van de acteur waarmee je wilt zoeken? (0 om te annuleren): ")

        if gebruiker_acteur_ID == "0":
            klaar_met_zoeken = True
        elif gebruiker_acteur_ID == "" or None:
            print("\nOngeldig invoer, voer een ID in.")
        else:
            resulaten_gekregen = zoek_film_acteur_lijst(gebruiker_acteur_ID)
            if resulaten_gekregen[0] is True:
                klaar_met_zoeken = True


def filter_release_datum(response=None):
    """
    Deze functie laat de zijn film lijst filteren via een release date
    """

    klaar_met_zoeken = False
    gefilterde_lijst_gekregen = False

    while not klaar_met_zoeken:
        gebruiker_release_datum = input("Met welk jaartal wil je filteren? (0 om te annuleren): ")

        if gebruiker_release_datum == "0":
            klaar_met_zoeken = True
        elif gebruiker_release_datum == "" or None:
            print("\nOngeldig invoer, voer een jaartal in.\n")
        else:
            if gefilterde_lijst_gekregen is False:
                gefilterde_lijst_gekregen = formateer_release_datum_film_lijst(response, gebruiker_release_datum)
                if gefilterde_lijst_gekregen is True:
                    klaar_met_zoeken = True
