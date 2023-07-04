class Sample:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        return self.a < other.a

    def __repr__(self):
        return str(self.a)


a = Sample(10)
b = Sample(20)

elements = [a, b]
print(sorted(elements, reverse=True))
