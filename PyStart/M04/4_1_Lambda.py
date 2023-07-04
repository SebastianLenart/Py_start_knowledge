"""
Filter - usuwanie elementow
Map - zmienianie elementow
Reduce - redukcja

function_name(callback, iterable)
callback - funkcja do zastosowania na elementach
iterable - lista, slownik

"""
# chcemy podwoic:
numbers = [1, 5, 10, 9, 7]
# tradycyjnie
doubles = [n + n for n in numbers]

# lambda:
doubles2 = map(lambda n: n+n, numbers)
print(doubles2)
print("-"*10)

#--------------------------------------------------------------
# tradycyjnie
filtered = [n for n in numbers if n % 2 ==0]

# lambda:
filtered2 = filter(lambda n: n % 2 == 0, numbers)

#--------------------------------------------------------------
from functools import reduce

numbers = [
    (1, 2),
    (3, 4),
    (5, 6),
]
# tradycyjnie
total = sum([a * b for a, b in numbers])
print(total)

# lambda:
total2 = reduce(lambda sum, a: sum + a[0] * a[1], numbers, 0) # 3 argumenty, 3ci => 0 to wartosc pocz.
print(total2) # w sum jest wynik poprzedniego dodawania













































