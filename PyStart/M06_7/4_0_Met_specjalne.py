"""
__init__ - utworzenie metody
__str__ - reprezentacja tekstowa
__add__ - dodanie dwoch obiektow (tak jak lista)
__eq__ - porownanie dwoch obiektow ==
__ge__ - porownanie obiektow >=
__le__ - porownanie obiektow <=
__lt__ - mniejsze niz
__gt__ - wieksze niz
__lte__ - <=
__gte__ - >=
__ne__ - !=
"""

class Student:
    def __init__(self, first_name: str, last_name: str, age: int):
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



me = Student("Kacper", "Lede", 22)
print(me)