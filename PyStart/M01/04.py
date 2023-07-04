# exercise 2

netto = float(input('Podaj wartosc netto: '))
vat = 0.23
brutto = netto + float(netto) * vat

print( f'Wartosc netto {netto}')
print(f'Wartosc vat: {vat*100}%')
print(f'Wartosc brutto: {brutto}')