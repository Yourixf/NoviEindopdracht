import config
from api.api_calls import api_calls_general as api_calls_general
from api.api_data_handling.api_data_handling_general import *
from api.api_data_handling.api_data_handling_movie import *
from api.api_data_handling.api_data_handling_actor import *


def terminal_logging():
    """
    Deze functie laat de gebruiker terminal logging uit of aanzetten
    """

    def print_optie_lijst():
        menu_optie = "aanzetten" if config.terminal_logging == False else "uitzetten"

        terminal_logging_optie_lijst = [
            "Wat wil je doen?\n",
            "1. Terug\n",
            f"2. Terminal logging {menu_optie} \n"
        ]

        print("".join(terminal_logging_optie_lijst))

    def print_status():
        if not config.terminal_logging:
            print("Terminal logging staat uit.\n")
        elif config.terminal_logging:
            print("Terminal logging staat aan.\n")

    print_status()
    print_optie_lijst()

    klaar_met_wijzigen = False

    while not klaar_met_wijzigen:
        gebruiker_optie_keuze = input("Maak een keuze: ")

        if gebruiker_optie_keuze == "1":
            klaar_met_wijzigen = True
        elif gebruiker_optie_keuze == "2":
            if not config.terminal_logging:
                config.terminal_logging = True
            elif config.terminal_logging:
                config.terminal_logging = False

            print_status()
            print_optie_lijst()

        elif gebruiker_optie_keuze not in ["1", "2", ]:
            print("Ongeldig invoer, voer een van de bovenstaande cijfer in zonder spaties of extra tekens")


def filter_genre(response=None):
    """
    Deze functie laat de beschikbare genres zien en laat de gebruiker de film lijst hiermee filteren

    Deze functie wordt aangeroepen vanuit hoofdmenu_optie_1() en krijgt de response mee, de functie
    roept de API een om de beschikbare genres te krijgen en weergeven, de gebruiker kiest hier 1 van
    en er wordt gecontroleerd of deze klopt, en als laatst wordt deze vergeleken met de film lijst in de response.
    """

    resulaten_gekregen, genre_dict = api_calls_general.krijg_beschikbare_film_genres()
    klaar_met_zoeken = False
    genre_film_lijst_gekregen = False

    while not klaar_met_zoeken:
        if genre_film_lijst_gekregen is False:
            gebruiker_genre_id = input("Wat is het ID van de genre? (zie lijst, 0 om te annuleren): ")

        if gebruiker_genre_id in genre_dict:
            genre_film_lijst_gekregen = formateer_genre_film_lijst(response, gebruiker_genre_id)
            klaar_met_zoeken = True
        elif gebruiker_genre_id == "0":
            klaar_met_zoeken = True
        elif gebruiker_genre_id not in genre_dict:
            print("Ongeldig invoer, vul een ID in zonder extra tekens of spaties.")


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
        else:
            if gefilterde_lijst_gekregen is False:
                gefilterde_lijst_gekregen = formateer_release_datum_film_lijst(response, gebruiker_release_datum)
                if gefilterde_lijst_gekregen is True:
                    klaar_met_zoeken = True


def filter_acteur_geslacht(response=None):
    """
    Deze functie laat de gebruiker de beschikbare geslacht opties zien, en laat de acteur lijst hiermee filteren.
    """

    geslacht_optie_lijst = [
        "1. Vrouw\n",
        "2. Man\n",
        "3. Non binair\n"
    ]

    print("".join(geslacht_optie_lijst))

    klaar_met_zoeken = False
    gefilterde_lijst_gekregen = False

    while not klaar_met_zoeken:
        gebruiker_acteur_geslacht = input("Met welk geslacht wil je filteren? (0 om te annuleren): ")

        if gebruiker_acteur_geslacht in ["1", "2", "3"]:
            if gefilterde_lijst_gekregen is False:
                gefilterde_lijst_gekregen = formateer_geslacht_acteur_lijst(response, gebruiker_acteur_geslacht)
                if gefilterde_lijst_gekregen is True:
                    klaar_met_zoeken = True
        elif gebruiker_acteur_geslacht == "0":
            klaar_met_zoeken = True
        elif gebruiker_acteur_geslacht not in ["0", "1", "2", "3"]:
            print("Ongeldig invoer, voer een van de bovenstaande cijfer in zonder spaties of extra tekens")
