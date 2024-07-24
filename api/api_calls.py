import requests

def krijg_authorisatie():
    #API_TOEGANG_TOKEN_AUTORISATIE = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3Mzg0OGUwNzI2NmRjZmZhNzJjMDMzYzQ4NDM5YzU4MSIsIm5iZiI6MTcyMTc4MDIwNS41MTcyNDEsInN1YiI6IjY2OWQyN2ZhMDU4MDdiY2Y0OTI2ODc2ZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.x-zhauI7vL9OIV56PrLbeeL-RW8dpg6a3eKtMvPiD_M"

    API_TOEGANG_TOKEN_AUTORISATIE = "73848e07266dcffa72c033c48439c581"
    return API_TOEGANG_TOKEN_AUTORISATIE


def test_api():
    #url = "https://api.themoviedb.org/3/search/movie?api_key=73848e07266dcffa72c033c48439c581"
    endpoint_url = "https://api.themoviedb.org/3/search/movie"

    query = f"&query=Iron Man&"
    url = endpoint_url + "?" + f"api_key={krijg_authorisatie()}" + query

    headers = {
        "accept": "application/json",
    }

    response = requests.get(url,headers=headers)

    #print(response.text)
    #print(response.json())

    for movie in response:
        print(movie[7])
def zoek_film_naam():

    API_ENDPOINT_URL = "https://api.themoviedb.org/3/search/movie"

    headers = {
        "accept": "application/json",
        "Authorization": f"{krijg_authorisatie()}",

    }

    response = requests.get(API_ENDPOINT_URL, headers)

    print(response.text)

test_api()
