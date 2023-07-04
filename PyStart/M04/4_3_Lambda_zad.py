def map_and_filter(numbers: list) -> list:
    sqrt = map(lambda x: x**0.5, numbers)
    return list(filter(lambda x: x % 2 == 0, sqrt)) # mozna zamiast sqrt dac cale wyrazenie

def test_map_and_filter():
    a = [16, 36, 25, 49]
    assert map_and_filter(a) == [4, 6]