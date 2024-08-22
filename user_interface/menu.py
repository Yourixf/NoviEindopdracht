import user_interface.menu as menu
import api.api_calls.api_calls_actor as api_calls_actor
import api.api_calls.api_calls_movie as api_calls_movie
import api.api_calls.api_calls_general as api_calls_general
import api.api_data_handling.api_data_handling_general as api_data_handling_general


def print_hoofdmenu():
    """
    Dit is een functie die het hoofdmenu print in de terminal

    """

    hoofd_opties_lijst = [
        "1. Zoek een film op basis van een titel\n",
        "2. Zoek acteur op basis van een naam\n",
        "3. Zoek een film door middel van een acteur\n"
        "4. Stop applicatie\n"
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
        "4. Filter lijst op genre"
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
            genre_film_lijst_gekregen = api_data_handling_general.formateer_genre_film_lijst(response, gebruiker_genre_id)
            klaar_met_zoeken = True
        elif gebruiker_genre_id == "0":
            klaar_met_zoeken = True
        elif gebruiker_genre_id not in genre_dict:
            print("Ongeldig invoer, vul een ID in zonder extra tekens of spaties.")


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
    resulaten_gekregen = None

    while not klaar_met_zoeken:
        if resulaten_gekregen is None or keuze_submenu == "2":
            gebruiker_acteur_naam = input("Wat is de naam van de acteur die je wilt opzoeken?: ")
            resulaten_gekregen = api_calls_actor.zoek_acteur_naam(gebruiker_acteur_naam)

        keuze_submenu = menu.submenu_optie_2(resulaten_gekregen)

        if keuze_submenu == "1":
            klaar_met_zoeken = True
        elif keuze_submenu == "3" and resulaten_gekregen == True:
            gebruiker_film_ID = input("Wat is het ID van de acteur? (zie lijst): ")
            api_calls_actor.zoek_acteur_details(gebruiker_film_ID)
        elif keuze_submenu not in ["1", "2", "3"]:
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
        "3. Weergeef details van een acteur\n"
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