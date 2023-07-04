value = "valueIfTrue" if 2 == 3 else "valueIfFalse"
print(value)
print("-------------------------")

experience = int(input("ile lat tu pracujecie"))
hoursOfWork = int(input("ile przepracowalas h w tym tyg?"))
itemSold = int(input("Ilosc sprzedanych produktow: "))
salary = 2500

experienceBonus = 0.1 if experience > 2 else 0.02 * experience
salesBonus = 0.25 if itemSold > 30 else 0
hoursOfWorkBonus = 0.08 if hoursOfWork > 160 and experience > 1 else 0.02

salaryBonus = salary + experienceBonus * salesBonus + salesBonus * salary + hoursOfWorkBonus * salary

print("Wynagrodzenie: ", salaryBonus)