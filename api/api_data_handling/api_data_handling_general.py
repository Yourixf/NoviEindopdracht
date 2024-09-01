import config
import textwrap


def formateer_maximale_grootte(value=None, max_length=50):
    """
    Deze functie zorgt ervoor dat de text grootte gemaximaliseerd is.

    Deze functie word aangeroepen vanuit andere functie die iets printen, en geven de
    print waarde een een max lengte, indien geen lente word geleverd is deze standaard 50
    en de waarde word geformateerd en geretouneerd.
    """
    if isinstance(value, str) and len(value) > max_length:
        return '\n'.join(textwrap.wrap(value, width=max_length))
    return value


def formateer_genre_lijst(response=None):
    """
    Deze functie formateert de genre lijst, gerkegen vanuit de API server.

    De functie zal over de data itereren, vervolgens formateren en presenteren aan de gebruiker.
    Tot slot zal deze een boolean waarde en genre lijst retourneren aan de aanroepende functie.
    """

    if response is not None:
        response_dict = response.json()

    genre_dict = {}

    if response is None:
        print("Er ging wat mis... Ik heb geen data meegekregen.")
        return False
    elif response_dict.get("genres", 0) == 0:
        print("Geen genres vanaf de server gekregen.\n")
        # Word geprint als logging variabele in main.py op True staat.
        if config.terminal_logging:
            print("Logging - Geen genres lijst weergegeven")
        return False
    else:
        print("-" * 50)
        print("Alle beschikbare genres vanuit de API server:\n")
        for genre in response_dict.get("genres", []):
            # De Get methode controleert of de waarde niet bestaat, en de strip methode vervangt de niet bestaande
            # met ONBEKEND, en deze waarde wordt via formateer_maximale_grootte gemaximaliseerd
            genre_id = formateer_maximale_grootte(str(genre.get("id", "")).strip() or "ONBEKEND")
            genre_name = formateer_maximale_grootte(str(genre.get("name", "")).strip() or "ONBEKEND")

            print(f"ID: {genre_id}, {genre_name}")
            genre_dict.setdefault(genre_id, genre_name)

        print("-" * 50, "\n")

        # Word geprint als logging variabele in main.py op True staat.
        if config.terminal_logging:
            print("Logging - Genre lijst weergegeven")

        return True, genre_dict
