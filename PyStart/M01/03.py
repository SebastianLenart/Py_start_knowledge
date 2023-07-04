# exercise 1

from math import floor # do zaokraglania np. w dol
height = int(input('Wzrost[cm]: '))
weight = float(input('Waga[kg]: '))
bmi = weight / (height / 100) ** 2

print(f'Dla wzrostu {height}')
print(f'i wagi {weight}')
# formatowanie (1 opcja)  i zaokraglanie (2 opcja), aby ograniczyc dluga liczbe

# opcja 1
#print(f'BMI wynosi {bmi:.2f}') # ogranicze cyfry po przecinku do 2 miejsc

# opcja 2
print(f'BMI wynosi {floor(bmi)}') # lub
print(f'BMI wynosi {round(bmi, 2)}') # do 2 miejsc po przecinku