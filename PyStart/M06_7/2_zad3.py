class Car:
    def __init__(self, name, price, max_speed):
        self.name = name
        self.price = price
        self.max_speed = int(max_speed)

    def get_info(self):
        return f"{self.name} {self.price} {self.max_speed}"


class Collection:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_items(self, key, reverse=False):
        return sorted(self.items, key=key, reverse=reverse)


if __name__ == "__main__":
    cars = []  # juz zbędne
    collection = Collection()
    for _ in range(3):
        name = input("Nazwa: ")
        price = int(input("Cena: "))
        max_speed = input("Vmax: ")
        car = Car(name, price, max_speed)
        collection.add_item(car)
        print("-" * 10)

        for car in collection.get_items(key=lambda c: c.price, reverse=True):
            print(car.get_info())


def test_class_car():
    car = Car(brand="Polonez", price=1000, max_speed=200)

    assert isinstance(car, Car)  # czy obiekt jest klasy Car
    assert car.name == "Polonez"
    assert car.price == 1000
    assert car.max_speed == 200
