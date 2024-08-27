import config
import user_interface.menu as menu
import api.api_calls.api_calls_actor as api_calls_actor
import api.api_calls.api_calls_movie as api_calls_movie
from methods.general_methods import *


def print_hoofdmenu():
    """
    Dit is een functie die het hoofdmenu print in de terminal

    """

    hoofd_opties_lijst = [
        "1. Zoek een film op basis van een titel\n",
        "2. Zoek acteur op basis van een naam\n",
        "3. Zoek een film door middel van een acteur\n"
        "4. Instellingen\n"
        "5. Stop applicatie\n"
    ]

    hoofd_menu = [
        f"{"-" * 30}\n",
        "Welkom in het hoofdmenu!\n",
        "Kies hieronder een van de acties via het cijfer.\n",
        "".join(hoofd_opties_lijst),
        f"{"-" * 30}\n",
    ]

    return print("".join(hoofd_menu))


def hoofdmenu_optie_1():
    """
    Deze functie haalt de film titel vanuit de gebruiker op en roept de api call functie aan

    Deze functie wordt aangeroepen vanuit start_applicatie en krijgt in deze functie een film titel die
    geretourneerd wordt naar api_calls.zoek_film_naam. Daar wordt de response geformateerd. Vervolgens
    Word de submenu_optie_1 aangeroepen om een vervolg actie uit te voeren.
    """
    klaar_met_zoeken = False
    keuze_submenu = None
    resulaten_gekregen = None

    while not klaar_met_zoeken:
        if resulaten_gekregen is None or keuze_submenu == "2":
            gebruiker_film_titel = input("Wat is de titel van de film die je wilt opzoeken?: ")
            resulaten_gekregen, response = api_calls_movie.zoek_film_naam(gebruiker_film_titel)

        keuze_submenu = menu.submenu_optie_1(resulaten_gekregen)

        if keuze_submenu == "1":
            klaar_met_zoeken = True
        elif keuze_submenu == "3" and resulaten_gekregen == True:
            gebruiker_film_ID = input("Wat is het ID van de film? (zie lijst): ")
            api_calls_movie.zoek_film_details(gebruiker_film_ID)
        elif keuze_submenu == "4" and resulaten_gekregen == True:
            filter_genre(response)
        elif keuze_submenu == "5" and resulaten_gekregen == True:
            filter_release_datum(response)
        elif keuze_submenu == "2":
            continue
        else:
            print("Ongeldig invoer, voer een van de bovenstaande cijfer in zonder spaties of extra tekens")
            continue


def submenu_optie_1(resulaten_gekregen=None):
    """
    Deze functie laat het submenu van optie 1 zien.

    Deze functie kijkt of de query resultaten bevat, indien wel wordt lijst versie 1 weergeven en andersom.
    """

    submenu_optie_lijst_versie_1 = [
        "\nWat wil je nu doen?\n",
        "1. Terug naar het hoofdmenu\n",
        "2. Een andere film titel zoeken\n",
        "3. Weergeef details van een film\n",
        "4. Filter lijst op genre\n",
        "5. Filter lijst op uitgave jaar\n"
    ]

    submenu_optie_lijst_versie_2 = [
        "\nWat wil je nu doen?\n",
        "1. Terug naar het hoofdmenu\n",
        "2. Een andere film titel zoeken\n"
    ]

    if resulaten_gekregen is False:
        print("".join(submenu_optie_lijst_versie_2))
    else:
        print("".join(submenu_optie_lijst_versie_1))

    keuze = input("Maak een keuze: ")

    return keuze


def hoofdmenu_optie_2():
    """
    Deze functie haalt een acteur naam en acteur ID vanuit de gebruiker op en roept de api call functie aan en
    retourneert de response.

    Deze functie wordt aangeroepen vanuit start_applicatie en loopt door deze fucntie menu heen tot dat de gebruiker
    de stop optie geeft. Deze functie krijgt vanuit de gebruiker een acteur naam, deze maakt wordt gebruikt in een api call,
    de response word geretourneerd en daarna geeft de gebruiker een acteur ID vanuit de response en hiermee wordt de details
    van een acteur gelaten zien.
    """

    klaar_met_zoeken = False
    keuze_submenu = None
    resultaten_gekregen = None

    while not klaar_met_zoeken:
        if resultaten_gekregen is None or keuze_submenu == "2":
            gebruiker_acteur_naam = input("Wat is de naam van de acteur die je wilt opzoeken?: ")
            resultaten_gekregen, response = api_calls_actor.zoek_acteur_naam(gebruiker_acteur_naam)

        keuze_submenu = menu.submenu_optie_2(resultaten_gekregen)

        if keuze_submenu == "1":
            klaar_met_zoeken = True
        elif keuze_submenu == "3" and resultaten_gekregen == True:
            gebruiker_film_ID = input("Wat is het ID van de acteur? (zie lijst): ")
            api_calls_actor.zoek_acteur_details(gebruiker_film_ID)
        elif keuze_submenu == "4" and resultaten_gekregen == True:
            filter_acteur_geslacht(response)
        elif keuze_submenu not in ["1", "2", "3", "4"]:
            print("Ongeldig invoer, voer een van de bovenstaande cijfer in zonder spaties of extra tekens")
            continue


def submenu_optie_2(resulaten_gekregen=None):
    """
    Deze functie laat het submenu van optie 1 zien.

    Deze functie kijkt of de query resultaten bevat, indien wel wordt lijst versie 1 weergeven en andersom.
    """

    submenu_optie_lijst_versie_1 = [
        "\nWat wil je nu doen?\n",
        "1. Terug naar het hoofdmenu\n",
        "2. Een andere film acteur zoeken\n",
        "3. Weergeef details van een acteur\n",
        "4. Filter op geslacht\n"
    ]

    submenu_optie_lijst_versie_2 = [
        "\nWat wil je nu doen?\n",
        "1. Terug naar het hoofdmenu\n",
        "2. Een andere acteur naam zoeken\n"
    ]

    if resulaten_gekregen is False:
        print("".join(submenu_optie_lijst_versie_2))
    else:
        print("".join(submenu_optie_lijst_versie_1))

    keuze = input("Maak een keuze: ")

    return keuze


def hoofdmenu_optie_3():
    """
    Deze functie haalt een acteur naam en acteur ID vanuit de gebruiker op en roept de api call functie aan en
    retourneert de response.

    Deze functie wordt aangeroepen vanuit start_applicatie en loopt door deze fucntie menu heen tot dat de gebruiker
    de stop optie geeft. Deze functie krijgt vanuit de gebruiker een acteur naam, deze maakt wordt gebruikt in een api call,
    de response word geretourneerd en daarna geeft de gebruiker een acteur ID vanuit de response en hiermee wordt een film lijst
    geretourneerd waar de actuer ID instaat. Hierna krijgt de gebruiker de opties om de bovenstaande functies te gebruiken.
    """

    klaar_met_zoeken = False
    keuze_submenu = None
    resulaten_gekregen = None

    while not klaar_met_zoeken:
        if resulaten_gekregen is None or keuze_submenu in ["2", "4"]:
            gebruiker_acteur_naam = input("Wat is de naam van de acteur die je wilt opzoeken?: ")
            resulaten_gekregen = api_calls_actor.zoek_acteur_naam(gebruiker_acteur_naam)

            if resulaten_gekregen == True:
                gebruiker_acteur_ID = input("Wat is het ID van de acteur waarmee je wilt zoeken?: ")
                resulaten_gekregen = api_calls_movie.zoek_film_acteur_lijst(gebruiker_acteur_ID)

        keuze_submenu = menu.submenu_optie_3(resulaten_gekregen)

        if keuze_submenu == "1":
            klaar_met_zoeken = True
        elif keuze_submenu == "3" and resulaten_gekregen == True:
            gebruiker_acteur_ID = input("Wat is het ID van de acteur waarvan je de details wilt zoeken?: ")
            api_calls_actor.zoek_acteur_details(gebruiker_acteur_ID)
        elif keuze_submenu not in ["1", "2", "3", "4"]:
            print("Ongeldig invoer, voer een van de bovenstaande cijfer in zonder spaties of extra tekens")
            continue


def submenu_optie_3(resulaten_gekregen=None):
    """
    Deze functie laat het submenu van optie 3 zien.

    Deze functie kijkt of de query resultaten bevat, indien wel wordt lijst versie 1 weergeven en andersom.
    """

    submenu_optie_lijst_versie_1 = [
        "\nWat wil je nu doen?\n",
        "1. Terug naar het hoofdmenu\n",
        "2. Een acteur zoeken\n",
        "3. Details weergeven van een acteur\n",
        "4. Films zoeken via een acteur ID\n"
    ]

    submenu_optie_lijst_versie_2 = [
        "\nWat wil je nu doen?\n",
        "1. Terug naar het hoofdmenu\n",
        "2. Een acteur zoeken\n"
    ]

    if resulaten_gekregen is False:
        print("".join(submenu_optie_lijst_versie_2))
    else:
        print("".join(submenu_optie_lijst_versie_1))

    keuze = input("Maak een keuze: ")

    return keuze


def hoofdmenu_optie_4():
    """
    Deze functie laat de gebruiker settings wijzigen in de applicatie.

    Deze functie wordt aangeroepen vanuit main.py, laat de huidige settings zien,
    en laat de gebruiker deze wijzigen.
    """

    def print_optie_lijst():
        settings_menu_lijst = [
            "\nWat wil je nu doen?\n",
            "1. Terug naar het hoofdmenu\n",
            "2. Terminal logging\n"
        ]

        print("".join(settings_menu_lijst))

    klaar_met_wijzigen = False

    print_optie_lijst()

    while not klaar_met_wijzigen:
        gebruiker_optie_keuze = input("Maak een keuze: ")

        if gebruiker_optie_keuze == "1":
            klaar_met_wijzigen = True
        elif gebruiker_optie_keuze == "2":
            terminal_logging()
            print_optie_lijst()
        elif gebruiker_optie_keuze not in ["1", "2"]:
            print("Ongeldig invoer, voer een van de bovenstaande cijfer in zonder spaties of extra tekens")
            continue
