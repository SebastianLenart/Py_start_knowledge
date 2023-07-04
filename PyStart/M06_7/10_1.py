from dataclasses import  dataclass

@dataclass
class Item:
    name: str
    price: float
    discount: float

class Collection:
    def __init__(self):
        self.items = [] # lista obiektow Item



    @classmethod
    def create_with_items(cls, *args): # bo dowolna ilosc argumentow
        collection = cls()
        collection.items.extend(args) # zamiast append, roznica znajdz

        return collection


it1 = Item("Chleb", 4, 0.1)
it2 = Item("Maslo", 3, 0.2)

col = Collection.create_with_items(it1, it2) # moge dowolna ilosc argumentow!
print(col.items) # da sie wyswietlic










