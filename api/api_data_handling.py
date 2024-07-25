import json

def formateer_film_lijst(response=None):
    """
    Deze functie formateert de flm lijst response.

    Deze functie kijkt eerst of er resultaten zijn, en indien er wel resultaten zijn word deze op een duidelijke manier
    weergegeven aan de gebruiker.
    """
    response_dict = response.json()
    formatted_json = json.dumps(response_dict, indent=1)

    print(f"{response_dict}")
    print(f"{formatted_json}")

    if response_dict["total_results"] == 0:
        return f"geen resultaten"
    else:
        for movie in response_dict["results"]:
            title = movie["title"]
            release_date = movie["release_date"]
            overview = movie["overview"]
            movie_id = movie["id"]

            print(f"Titel: {title}")
            print(f"Release Datum: {release_date}")
            print(f"Overzicht: {overview}")
            print(f"Film ID nummer: {movie_id}")
            print("___")

def formateer_film_details(response=None):
    """
    Deze functie formateert de film details response.
    """

    response_dict = response.json()
    formatted_json = json.dumps(response_dict, indent=1)

    print(response_dict["adult"])

