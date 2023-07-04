x1 = int(input('Podaj x wierzcholka 1: '))
y1 = int(input('Podaj y wierzcholka 1: '))

x2 = int(input('Podaj x wierzcholka 2: '))
y2 = int(input('Podaj x wierzcholka 2: '))

x3 = int(input('Podaj x wierzcholka 3: '))
y3 = int(input('Podaj x wierzcholka 3: '))

area = abs((x2-x1) * (y3-y1) - (y2-y1) *(x3-x1))/2
print(f'Pole trojkata wynosi {area}')