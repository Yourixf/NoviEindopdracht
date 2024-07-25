def controleer_status_code(response=None):

    if response.status_code == 200:
        return 200, "Succesvol."
    elif response.status_code == 400:
        return 400, "'Bad Request', de server snapt jouw verzoek niet. Probeer het opnieuw."
    elif response.status_code == 401:
        return 401, "'Unauthorized', je hebt geen toegang om deze actie uit te voeren."
    elif response.status_code == 403:
        return 403, "'Forbidden', je hebt geen rechten om deze actie uit te voeren."
    elif response.status_code == 404:
        return 404, "'Not Found', de server heeft jouw verzoek niet kunnen vinden op de server "
    elif response.status_code == 429:
        return 429, "'Rate limit exceeded', je bent over je toegestaande hoeveelheid verzoeken heen."

