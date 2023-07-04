summary = 1
done = False
while  not done:
    value = input('Prosze podac liczbe lub koniec aby zakonczyc')
    if value == "koniec":
        done = True
        continue
    number = int(value)
    if number % 2 == 0:
        summary *= number

print("Iloczy wartosci parzystych", summary)