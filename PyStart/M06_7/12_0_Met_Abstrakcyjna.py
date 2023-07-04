from abc import ABC, abstractmethod

class Item(ABC): # klasa obstakcyjna
    def __init__(self, name, price):
        self.name = name
        self. price = price

    @abstractmethod
    def get_total_price(self):
        pass

class Product(Item):

    def get_total_price(self):
        return self.price

"""

Metody abstrakcyjne to tak samo jak w c++

"""













