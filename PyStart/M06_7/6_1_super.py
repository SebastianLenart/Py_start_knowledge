class Product:
    def __init__(self, price):
        self.price = price

    def get_price(self):
        return self.price


class DiscountedProduct(Product):
    def get_price(self):
        price= super().get_price()
        return price - 0.1 * price

product = DiscountedProduct(100)
print(product.get_price())

# SUPER !!! uzywamy dla metod powtarzajacych sie z parent i child !
# klasa wyzej nie powinna korzystac z metod klasy nizej