"""
Metody klasowe tworza nowe obiekty wygodniej

"""

class Person:
    def __init__(self, firt_name: str, last_name: str):
        self.first_name = firt_name
        self.last_name = last_name


    @classmethod
    def from_row(cls, row: str):
        # Jan;Kowalski
        first_name, last_name = row.strip().split(';')
        return cls(first_name, last_name)

p = Person("Kacper", "Sier")
pp = Person.from_row("Kacper;Sieradz") # nowy obiekt inaczej zrobiony
print(p.first_name)
print(p.last_name)
print("*"*10)
print(pp.first_name)
print(pp.last_name)

































