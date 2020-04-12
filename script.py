import requests
from country_list import countries_for_language

countries = dict(countries_for_language('en'))

while (True):
    for country in countries.values():
        print(requests.get(
            "http://127.0.0.1:8000/entities/{country} considers banning sidewalk delivery robots".format(
                country=country)).json())
