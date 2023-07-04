from urllib.request import urlopen
from json import loads

with urlopen("http://api.nbp.pl/api/exchangerates/tables/A/") as site:
    # print(site.read().decode("utf-8")) # zeby bylo w string i mozna bylo wyswietlic
    data = loads(site.read().decode("utf-8"))
    # print(data[0]["rates"])
    rates = data[0]["rates"]

    exchange = input("jaka wartosc chcesz wymienic na PLN")
    value, code = exchange.split(" ")
    value = float(value)

    rate = list(filter(lambda  x: x["code"] == code, rates))
    print(f"Otrzymujesz {value * rate[0]['mid']} PLN")