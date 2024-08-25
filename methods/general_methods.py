from api.api_calls import api_calls_general as api_calls_general
from api.api_data_handling import api_data_handling_general as api_data_handling_general


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
