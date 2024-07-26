import api.api_calls as api_calls


def print_hoofdmenu():
    """
    Dit is een functie die het hoofdmenu print in de terminal

    """

    hoofd_opties_lijst = [
        "1. Zoek een film op basis van een titel\n",
        "2. Zoek films op basis van een genre\n",
        "3. Zoek een acteur op basis van een naam\n",
        "4. Zoek een film door middel van een acteur\n"
        "5. Stop applicatie\n"
    ]

    hoofd_menu = [
        "|||||||||||||||||||||||||||||||\n",
        "Welkom in het hoofdmenu!\n",
        "Kies hieronder een van de acties via het cijfer.\n",
        "".join(hoofd_opties_lijst),
        "|||||||||||||||||||||||||||||||\n"
    ]

    return print("".join(hoofd_menu))


def hoofdmenu_optie_1():
    """
    Deze functie haalt de film titel vanuit de gebruiker op en roept de api call functie aan

    Deze functie word aangeroepen vanuit start_applicatie en krijgt in deze functie een film titel die
    ge retourneerd word naar api_calls.zoek_film_naam daarvanuit komt er een submenu keuze terug, daarna word de gebruiker
    deze functie naar de gewenste optie gestuurd.
    """
    klaar_met_zoeken = False

    while not klaar_met_zoeken: #TO DO FIX LOOP, 404 ERROR EN MELDING RESULTATEN GEKREGEN
        gebruiker_film_titel = input("Wat is de titel van de film die je wilt opzoeken?: ")

        keuze_submenu = api_calls.zoek_film_naam(gebruiker_film_titel)

        klaar_met_zoeken = True if keuze_submenu == "1" else False

        if keuze_submenu == "3":
            gebruiker_film_ID = input("Wat is het ID van de film? (zie hierboven): ")
            uitgevoerd = api_calls.zoek_film_details(gebruiker_film_ID)
            if uitgevoerd == True:
                submenu_optie_1(False)

def submenu_optie_1(resulaten_gekregen=None):
    """
    Deze functie laat het submenu van optie 1 zien.

    Deze functie kijkt of de query resultaten bevat, indien wel wordt lijst versie 1 weergeven en andersom.
    """

    submenu_optie_lijst_versie_1 = [
        "\nWat wil je nu doen?\n",
        "1. Terug naar het hoofdmenu\n",
        "2. Een andere film titel zoeken\n",
        "3. Weergeef details van een film\n"
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
