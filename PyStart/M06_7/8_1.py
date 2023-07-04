capitals = {
    "Poland": "Warsaw",
    "Germany": "Berlin"
}
try:
    country = input("Podaj nazwe panstwa: ")
    print(capitals[country])
except KeyError:
    print(f"Nie ma takiego klucza")






















