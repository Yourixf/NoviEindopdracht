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
    gebruiker_film_titel = input("Wat is de titel van de film die je wilt opzoeken?: ")

    if gebruiker_film_titel != None:
        return print("functie aangeroepen.")


def start_applicatie():
    """
    Dit is de hoofdfunctie van de applicatie die het programma initialiseerd.

    Deze ontvangt en verstuurd gegevens op basis van input.
    """
    stop_applicatie = False

    while not stop_applicatie:
        print_hoofdmenu()
        gebruiker_menu_keuze = input("Welke optie wil je kiezen?: ")

        if gebruiker_menu_keuze == "5":
            stop_applicatie = True
        elif gebruiker_menu_keuze == "1":
            print("Je hebt voor optie 1 gekozen.")
            hoofdmenu_optie_1()
        elif gebruiker_menu_keuze == "2":
            print("Je hebt voor optie 2 gekozen.")
        elif gebruiker_menu_keuze == "3":
            print("Je hebt voor optie 3 gekozen.")
        elif gebruiker_menu_keuze == "4":
            print("Je hebt voor optie 5 gekozen.")
        else:
            print("Geen geldige keuze! Maak een keuze doormiddel van een cijfer zonder spaties.")


