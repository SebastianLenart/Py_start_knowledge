from json import loads
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
country = input("Podaj kraj: ")

try: # moze byc literowka w url ponizej
    with urlopen(f"https://restcountries.eu/rest/v2/name/{country}") as response:
        data = loads(response.read().decode("utf-8")) # jako string
        print(data)
        country_data = data[0]
        print("Stolica", country_data["capital"])
except (URLError, HTTPError) as error:
    print(error)
    print("blad komunikacji")


# https://restcountries.eu/rest/v2/name/Polska