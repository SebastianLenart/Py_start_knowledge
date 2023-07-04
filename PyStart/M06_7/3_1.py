class Apple:
    def __init__(self, color: str, taste: str, kind: str):
        self.color = color
        self.taste = taste
        self.kind = kind


class Basket:
    def __init__(self):
        self.apples = []

    def add(self, apple: Apple):
        self.apples.append(apple)


class Report:
    def __init__(self, basket: Basket):
        self.basket = basket

    def get_for_color(self):
        report = {}
        for apple in self.basket.apples:
            if apple.color not in report:
                report[apple.color] = 0
            report[apple.color] += 1
        return report


def test_apples_collection():
    # given
    apple1 = Apple("Czerwone", "Slodkie", "Dojrzale")
    apple2 = Apple("Czerwone", "Slodkie", "Niedojrzale")
    apple3 = Apple("Zielone", "Kwasne", "Dojrzale")
    basket = Basket()

    # when
    basket.add(apple1)
    basket.add(apple2)
    basket.add(apple3)

    report = Report(basket)
    colors = report.get_for_color()

    # then
    assert colors == {
        "Czerwone": 2,
        "Zielone": 1
    }

# python -m pytest 3_1.py