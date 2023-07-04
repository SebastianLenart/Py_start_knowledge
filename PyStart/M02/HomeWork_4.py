pesel = "98022410251"
check = "13791379131"

control = 0
for index, _ in enumerate(pesel):
    control += int(pesel[index]) * int(check [index])

print(control)
if str(control)[-1] == '0':
    print("pesel jest OK")
else:
    print("Pesel jest zly")