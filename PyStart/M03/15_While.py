"""

bus_capacity = 100
passengers_in_bus = 0

while bus_capacity >= passengers_in_bus:
    passengers_in_bus += int(input("Ile osob weszło"))

    if passengers_in_bus > bus_capacity:
        print(f'Ostatnie {passengers_in_bus-bus_capacity} musi wyjsc, eloo')

print("jadym")

"""
"""

values = []
while len(values) <= 5:
    value = int(input("Podaj liczbe"))
    if value > 0:
        values.append(value)

print(max(values), min(values))

"""

done = False
value = int(input("Podaj 1sza liczbe"))
values = [value]  # value
while not done:
    value2 = int(input("Podaj liczbe"))
    values.append(value2)
    if value2 < value:
        done = True
        continue
    else:
        values.append(value2)

    value = value2

print(sum(values)/len(values))