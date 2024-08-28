import user_interface.menu as menu


def start_applicatie():
    """
    Dit is de hoofdfunctie van de applicatie die het programma initialiseerd.

    Deze ontvangt en verstuurd gegevens op basis van input.
    """
    stop_applicatie = False

    while not stop_applicatie:
        menu.print_hoofdmenu()
        gebruiker_menu_keuze = input("Welke optie wil je kiezen?: ")

        if gebruiker_menu_keuze == "5":
            stop_applicatie = True
        elif gebruiker_menu_keuze == "1":
            print("\nJe hebt voor optie 1 gekozen.\n")
            menu.hoofdmenu_optie_1()
        elif gebruiker_menu_keuze == "2":
            print("\nJe hebt voor optie 2 gekozen.\n")
            menu.hoofdmenu_optie_2()
        elif gebruiker_menu_keuze == "3":
            print("\nJe hebt voor optie 3 gekozen.\n")
            menu.hoofdmenu_optie_3()
        elif gebruiker_menu_keuze == "4":
            print("\nJe hebt voor optie 4 gekozen.\n")
            menu.hoofdmenu_optie_4()
        #elif gebruiker_menu_keuze == "20":
        #    api.api_calls.api_calls_movie.zoek_film_acteur_lijst("Ryan Reynolds")
        else:
            print("\nGeen geldige keuze! Maak een keuze doormiddel van een cijfer zonder spaties.\n")


start_applicatie()