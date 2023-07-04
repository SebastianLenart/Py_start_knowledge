def get_sum(list1: list, list2: list):
    total = []
    return [a + b for a, b in zip(list1, list2)]


print(get_sum([1, 2, 3], [4, 5, 6]))
