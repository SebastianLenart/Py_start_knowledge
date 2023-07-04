class Product:
    def __init__(self, price):
        self.price = price
        self._discount = 0.1

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, new_discount):
        if 0 < new_discount < 1:
            self._discount = new_discount


    @discount.deleter
    def discount(self):
        del self._discount

car = Product(1000)
print(car.discount)
del car.discount
print(car.discount)


"""
COS NIE DZIALA !!!

"""





