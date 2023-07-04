names = [
    "Wojtek",
    "Krysia",
    "Basia",
    "Wiola",
    "Antek",
    "Aneta",
    "Ksawery"
]


for id, name in enumerate(names):
    print(f"{id}. {name}")
try:
    number = int(input("Które imie wybierasz?"))
    print(names[number]) # musi byc klucz
except IndexError:
    print("Nie ma takiego imienia")
except (TypeError, ValueError) as error:
    print("Nie rozumiem")
    print(error)


















