from operator import ne

print([n + n for n in range(1, 11)])
# ----------------------------------------------

newList1 = []
for n in range(1, 11):
    if n % 2 == 0:
        newList1.append("even")
    else:
        newList1.append("odd")
print(newList1)

# szybciej
newList2 = ["even" if n % 2 == 0 else "odd" for n in range(1, 11)]
print(newList2)

# filtrowanie
names = ["sebastian", "martyna", "olga", "jan"]
ladies = [name for name in names if name[-1] == "a"]
print(ladies)
print("----------------------------------------")

persons = [
    ("janek", "wisniewski", "gdynia"),
    ("Grzegorz", "Turtuj", "Kotorydz"),
    ("Syrenka", "warszawska", "warszawa"),
]
personsG = [person for person in persons if person[-1][0] == 'g']
print(personsG)
personUpp = [(person[0], person[1], person[2].upper()) for person in personsG]
print(personUpp)
print("----------------------------------------")
# inaczej
personUpp2 = [(person[0], person[1], person[2].upper()) for person in persons if person[-1][0] == 'g']
print(personUpp2)




