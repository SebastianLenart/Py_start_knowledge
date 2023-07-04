
# opcja 2
while True:
    try:
        value = int(input("Podaj liczbe: "))
        if not value % 5 == 0:
            raise Exception("Liczba nie jest podzielna przez 5. ")

        print(value)

    except Exception as e:
        print(e)

# opcja 1
while True:
    value = int(input("Podaj liczbe: "))
    if not value % 5 == 0:
        raise Exception("Liczba nie jest podzielna przez 5. ")

    print(value)


# opcja 3
try:
    while True:
        value = int(input("Podaj liczbe: "))
        if not value % 5 == 0:
            raise Exception("Liczba nie jest podzielna przez 5. ")

        print(value)

except Exception as e:
    print(e)















