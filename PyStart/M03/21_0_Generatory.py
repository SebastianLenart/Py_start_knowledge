# bez generatora
def getDoubles(numbers: range):
    results = []
    for i in numbers:
        results.append(i + i)
    return results


for n in getDoubles(range(1, 11)):
    print(f'Wynik wynosi {n}')


# -----------------------------------------------------------
# generator
def getDoubles2(numbers: range):
    for i in numbers:
        print(f'Iteruje.. liczbe dla {i}')
        yield i + i


results = getDoubles2(range(1, 11))
print(next(results))
print(next(results))
results.close() # zatrzymanie
print(next(results))
print("-------------------------------------------------")

