def controleer_status_code(response=None):
    """
    Deze functie conttoleert de status code van de API request.

    Deze functie ontvangt van diverse API request functies de response, en controleert
    of welke status code deze heeft en deze word met een bericht geretourneerd.

    """

    if response.status_code == None:
        return 0, "De server geeft geen response"
    elif response.status_code == 200:
        return 200, "Succesvol.\n"
    elif response.status_code == 400:
        return 400, "'Bad Request', de server snapt jouw verzoek niet. Probeer het opnieuw.\n"
    elif response.status_code == 401:
        return 401, "'Unauthorized', je hebt geen toegang om deze actie uit te voeren.\n"
    elif response.status_code == 403:
        return 403, "'Forbidden', je hebt geen rechten om deze actie uit te voeren.\n"
    elif response.status_code == 404:
        return 404, "'Not Found', de server heeft jouw verzoek niet kunnen vinden op de server.\n"
    elif response.status_code == 429:
        return 429, "'Rate limit exceeded', je bent over je toegestaande hoeveelheid verzoeken heen.\n"

