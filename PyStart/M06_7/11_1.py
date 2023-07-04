from datetime import datetime

class Product:
    def __init__(self, price):
        self.price = price

    def calculate_netto(self):
        return self.price

    def calculate_brutto(self):
        return self.price * 1.23


class Booking:
    def __init__(self, date_start: datetime, date_end: datetime):
        self.date_end = date_end
        self.date_start = date_start

    def get_difference(self):
        diff = self.date_end - self.date_start
        return diff.days + 1 # (nie)liczymy noce


class Reservation(Product, Booking):
    def __init__(self, price: float, date_start: datetime, date_end: datetime):
        Product.__init__(self, price)
        Booking.__init__(self, date_start, date_end)

    def calculate_total(self):
        return self.calculate_brutto() * self.get_difference()


stay = Reservation(100, datetime(2020, 6, 1), datetime(2020, 6, 7))
print(stay.calculate_total())















