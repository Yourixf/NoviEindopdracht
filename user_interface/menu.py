import user_interface.menu as menu
from methods.helper_methods_actor import krijg_acteur_lijst, krijg_acteur_details, filter_acteur_geslacht
from methods.helper_methods_general import *
from methods.helper_methods_movie import krijg_film_lijst, krijg_film_details, filter_release_datum, \
    krijg_film_acteur_lijst


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
        f"{'-' * 30}\n",
        "Welkom in het hoofdmenu!\n",
        "Kies hieronder een van de acties via het cijfer.\n",
        "".join(hoofd_opties_lijst),
        f"{'-' * 30}\n",
    ]

    return print("".join(hoofd_menu))


def hoofdmenu_optie_1():
    """
    Deze functie laat de gebruiker in de hoofdmenu optie 1 navigeren en diverse functies gebruiken.

    Deze functie wordt aangeroepen vanuit start_applicatie. De gebruiker maakt een keuze, hierna zal de gebruiker
    naar de betreffende functie worden gestuurd. Vervolgens wordt submenu_optie_1 aangeroepen om een vervolg actie uit
    te voeren.
    """
    klaar_met_zoeken = False
    keuze_submenu = None
    resulaten_gekregen = None

    while not klaar_met_zoeken:
        if resulaten_gekregen is None or keuze_submenu == "2":
            resulaten_gekregen, response = krijg_film_lijst()

        keuze_submenu = menu.submenu_optie_1(resulaten_gekregen)

        if keuze_submenu == "1":
            klaar_met_zoeken = True
        elif keuze_submenu == "3" and resulaten_gekregen == True:
            krijg_film_details()
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
    Deze functie laat de gebruiker in de hoofdmenu optie 2 navigeren en diverse functies gebruiken.

    Deze functie wordt aangeroepen vanuit start_applicatie. De gebruiker maakt een keuze, hierna zal de gebruiker
    naar de betreffende functie worden gestuurd. Vervolgens wordt submenu_optie_1 aangeroepen om een vervolg actie uit
    te voeren.
    """

    klaar_met_zoeken = False
    keuze_submenu = None
    resultaten_gekregen = None

    while not klaar_met_zoeken:
        if resultaten_gekregen is None or keuze_submenu == "2":
            resultaten_gekregen, response = krijg_acteur_lijst()

        keuze_submenu = menu.submenu_optie_2(resultaten_gekregen)

        if keuze_submenu == "1":
            klaar_met_zoeken = True
        elif keuze_submenu == "3" and resultaten_gekregen == True:
            krijg_acteur_details()
        elif keuze_submenu == "4" and resultaten_gekregen == True:
            filter_acteur_geslacht(response)
        elif keuze_submenu not in ["1", "2", "3", "4"]:
            print("Ongeldig invoer, voer een van de bovenstaande cijfer in zonder spaties of extra tekens")
            continue


def submenu_optie_2(resulaten_gekregen=None):
    """
    Deze functie laat het submenu van optie 2 zien.

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
    Deze functie laat de gebruiker in de hoofdmenu optie 3 navigeren en diverse functies gebruiken.

    Deze functie wordt aangeroepen vanuit start_applicatie. De gebruiker maakt een keuze, hierna zal de gebruiker
    naar de betreffende functie worden gestuurd. Vervolgens wordt submenu_optie_1 aangeroepen om een vervolg actie uit
    te voeren.
    """

    klaar_met_zoeken = False
    keuze_submenu = None
    resulaten_gekregen = None

    while not klaar_met_zoeken:
        if resulaten_gekregen is None or keuze_submenu in ["2", "4"]:
            resulaten_gekregen, response = krijg_acteur_lijst()

            if resulaten_gekregen is True:
                krijg_film_acteur_lijst()

        keuze_submenu = menu.submenu_optie_3(resulaten_gekregen)

        if keuze_submenu == "1":
            klaar_met_zoeken = True
        elif keuze_submenu == "3" and resulaten_gekregen == True:
            krijg_acteur_details()
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

    Deze functie wordt aangeroepen vanuit main.py, laat de huidige settings zien, en laat de gebruiker deze wijzigen
    via de bijbehorende helper functie.
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
