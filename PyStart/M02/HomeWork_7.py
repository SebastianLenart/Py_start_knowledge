from math import floor

min =int(input("Podaj wartosc najmniejsza: "))
max =int(input("Podaj wartosc najwieksza: "))

for number in range(min, max +1):
    is_prime = True
    for divider in range(2, floor(number**0.5) + 1): # czemu takie rownanie?
        if number % divider == 0:
            is_prime = False
            break
    if is_prime:
        print(number) # liczby pierwsze


