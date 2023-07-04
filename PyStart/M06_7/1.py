from math import pi


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_field(self):
        return pi * self.radius ** 2


if __name__ == "__main__": # co to jest
    r = int(input("Podaj promien: "))
    circle = Circle(r)
    print(f"Pole: {circle.calculate_field():.2f}")

def test_circle_field():
    # given
    r = 10
    c = Circle(r)

    # when
    field = c.calculate_field()

    # then
    assert field == pi * r * r


