import sys
import requests
from pycountry import countries

api_key = ""

def parse_country_name(country_name):
    try:
        return countries.search_fuzzy(country_name)[0].name
    except LookupError:
        raise KeyError("Invalid country was specified")


def get_distance(fcountry, scountry):
    resp = requests.post(
        url="https://distanceto.p.rapidapi.com/distance/route",
        json={"route":[{"name":fcountry},{"name":scountry}]},
        headers={"x-rapidapi-key": api_key, "x-rapidapi-host": "distanceto.p.rapidapi.com", "Content-Type": "application/json"}
    )

    return (int(resp.json()['route']['haversine']) + 1)

#
if __name__ == "__main__":
    if len(sys.argv) == 2:
        api_key = sys.argv[1]
    else:
        raise TypeError("Missing API Key")
    
    fcountry = input("First Country: ")
    scountry = input("Second Country: ")

    get_distance(parse_country_name(fcountry), parse_country_name(scountry))