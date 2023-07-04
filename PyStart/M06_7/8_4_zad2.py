fruits = []

try:
    for _ in range(0, 10):
        fruit = input("Podaj nazwe owoca: ")
        if fruit in fruits:
            raise ValueError("Ten owoc juz jest")

        fruits.append(fruit)
except ValueError as e:
    print(e)


"""
Wlasny wyjatek inny niz np ValueError:
tworzymy klase dziedziczaca po Exception

w niektorych bibliotekach jest np ze serwer nie odpowieada w jakis czasie itd

"""


class ValueToSmall(Exception):
    pass

class ValueToBig(Exception):
    pass

try:
    value = int(input("Podaj liczbe: "))
    if value < 10:
        raise ValueToSmall()
    if value > 20:
        raise  ValueToBig()

    print(value)

except(ValueToSmall, ValueToBig) as error:
    print(error)






