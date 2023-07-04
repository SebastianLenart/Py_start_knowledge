list1 = [5, 4, 1, 5]
list2 = [6, 7, 8, 2, 1, 5]  # nadmiar ucina
list3 = [9, 3, 5, 1, 3]  # nadmiar ucina

print(list(zip(list1, list2, list3)))

#-------------------------------------------------------------

print("-------------------")
first_names = ["zofia", "Seba", "Ala"]
last_names = ["Lenart", "kot", "pies"]
for first_names, last_names in zip(first_names, last_names): # łączy w krotke chyba
    print(first_names, last_names)

#-------------------------------------------------------------
print("-------------------")
# zadanie z peselem, update
pesel = "98022410251"
check = "13791379131"

control = 0
for pesel_digit, check_digit in zip(pesel, check): # łączy w krotke chyba
    control += int(pesel_digit) * int(check_digit)

print(control)
if str(control)[-1] == '0':
    print("pesel jest OK")
else:
    print("Pesel jest zly")



