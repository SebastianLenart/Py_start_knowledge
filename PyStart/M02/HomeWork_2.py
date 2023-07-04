option = input("Co chcesz zamienic? 1-binarna, 2-dziesietna")
if option == "1":
    value = input("Podaj wartosc w systemie dwojkowym")
    result = 0
    for index, number in enumerate(value):
        result += int(number) * 2 ** (len(value) - index - 1)
        print("result", result)  # 4, 6, 7
elif option == "2":
    # opcja 1
    value = int(input("Podaj wartosc w systemie dziesietnym"))
    print(f'Value {value:b}') # zamienia nam na dwojkowy
    # opcja 2
    # zrób recznie to zadanie
else:
    print("Nie wiem co wybrac")
