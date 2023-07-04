class Box:
    def __init__(self, capacity):
        self.capacity = capacity

    def __str__(self):
        return f"Box({self.capacity})"

    def __lt__(self, other): # less then mniejszy niz
        return self.capacity < other.capacity


boxes = [
    Box(10),
    Box(40),
    Box(20),
]

for box in sorted(boxes):
    print(box)
