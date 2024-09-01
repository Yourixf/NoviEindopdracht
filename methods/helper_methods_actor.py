from api.api_calls.api_calls_actor import zoek_acteur_naam, zoek_acteur_details
from api.api_data_handling.api_data_handling_actor import formateer_geslacht_acteur_lijst


def krijg_acteur_lijst():
    """
    Deze functie laat de gebruiker via een acteur naam zoeken naar een acteur.

    De gebruiker zal voor een acteur naam worden grevraagd, deze input wordt gecontroleerd. Indien oke, zal deze
    gebruikt worden in een api call.
    """

    klaar_met_zoeken = False
    resultaten_gekregen = False, {}

    while not klaar_met_zoeken:
        gebruiker_acteur_naam = input("Wat is de naam van de acteur die je wilt opzoeken? (0 om te annuleren): ")

        if gebruiker_acteur_naam == "0":
            klaar_met_zoeken = True
        elif gebruiker_acteur_naam == "" or None:
            print("\nOngeldig invoer, voer een naam in.\n")
        else:
            resultaten_gekregen = zoek_acteur_naam(gebruiker_acteur_naam)
            if resultaten_gekregen[0] is True:
                klaar_met_zoeken = True

    if klaar_met_zoeken is True:
        return resultaten_gekregen


def krijg_acteur_details():
    """
    Deze functie laat de gebruiker via een acteur ID de acteur details zoeken en weergeven.

    De gebruiker zal voor een acteur ID worden grevraagd, deze input wordt gecontroleerd. Indien oke, zal deze
    gebruikt worden in een api call.
    """
    klaar_met_zoeken = False

    while not klaar_met_zoeken:
        gebruiker_acteur_ID = input("Wat is het ID van de acteur? (zie lijst, 0 om te annuleren): ")

        if gebruiker_acteur_ID == "0":
            klaar_met_zoeken = True
        elif gebruiker_acteur_ID == "" or None:
            print("\nOngeldig invoer, voer een ID in.\n")
        else:
            details_gekregen = zoek_acteur_details(gebruiker_acteur_ID)
            if details_gekregen is True:
                klaar_met_zoeken = True


def filter_acteur_geslacht(response=None):
    """
    Deze functie laat de gebruiker de beschikbare geslacht opties zien, en laat de acteur lijst hiermee filteren.

    De gebruiker zal om een geslacht optie worden grevraagd, deze input wordt gecontroleerd. Indien oke, zal deze
    gebruikt worden in formateer functie.
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
