import user_interface.menu as menu
import user_interface.user_error_handling as user_error_handling



def start_applicatie():
    """
    Dit is de hoofdfunctie van de applicatie die het programma initialiseerd.

    Deze ontvangt en verstuurd gegevens op basis van input.
    """
    stop_applicatie = False

    #als je deze op True zet zie je de logging van mijn functies in de terminal terug, bijvoorbeeld server status code.
    terminal_logging = False

    while not stop_applicatie:
        menu.print_hoofdmenu()
        gebruiker_menu_keuze = input("Welke optie wil je kiezen?: ")

        if gebruiker_menu_keuze == "5":
            stop_applicatie = True
        elif gebruiker_menu_keuze == "1":
            print("Je hebt voor optie 1 gekozen.")
            menu.hoofdmenu_optie_1()
        elif gebruiker_menu_keuze == "2":
            print("Je hebt voor optie 2 gekozen.")
        elif gebruiker_menu_keuze == "3":
            print("Je hebt voor optie 3 gekozen.")
        elif gebruiker_menu_keuze == "4":
            print("Je hebt voor optie 4 gekozen.")
        else:
            print("Geen geldige keuze! Maak een keuze doormiddel van een cijfer zonder spaties.")


start_applicatie()
