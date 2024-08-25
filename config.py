# als je deze op True zet zie je de logging van mijn functies in de terminal terug, bijvoorbeeld server status code.
terminal_logging = False

def krijg_authorisatie():
    """
    Deze functie word voorziet andere API call functies van authorisatie.

    Deze functie retourneert mijn persoonlijke API Key in de API_KEY_AUTHORISATIE constante variabel
    aan de functie die een API endpoint aanroept zodat deze toegang krijgt.
    """

    API_KEY_AUTHORISATIE = "73848e07266dcffa72c033c48439c581"
    return API_KEY_AUTHORISATIE
