charakter = dict(firstName="Seba", lastName="Lenart")
print(charakter)
print(charakter.values())  # mozna z tego zrobic liste
print(charakter.keys())
print("----------------------------------------------")

products = {
    "granaty": 3.5,
    "czarny proch": 10,
    "mp40": 100,
    "kalasznikov": 1500
}

# gdy nie ma klucza w slowniku np.:
# print(products["ak47"]) # blad, ale jest na to sposob
print(products.get("ak47", "unknown"))

for product in products:
    print(product, products[product])

print("----------------------------------------------")

for product in products.items():
    print(product)
    print(product[0], product[1])

# quit()  # konczy program

print("----------------------------------------------")
for name, price in products.items():
    print(name, price)

# sprawdenie czy cos jest w slowniku w kluczy albo w wartosci

# w kluczu
if "granaty" in products:
    print("jest")
else:
    print("nie ma")

# w wartosci
if 1500 in products.values():
    print("jest")
else:
    print("nie ma")

print("----------------------------------------------")

polAng = {
    "pies": "dog",
    "chomik": "hamster",
    "papuga": "parrot",
    "kot": "cat"
}

angPol = {}

for polish, english in polAng.items():
    angPol[english] = polish
print(angPol)

question = input("[1] pol-ang, [2] ang-pol")
if question not in ["1", "2"]:
    quit()
# ...
