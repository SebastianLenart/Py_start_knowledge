from datetime import date

today = date.today()
print(f"Today: {today}")

formatted = today.strftime("%a.%A.%w.%d.%b.%B.%m.%Y")
print(formatted)

#-------------------------------------------------------------

dayB = date(today.year, 2, 24)
birthday = dayB.strftime("%d.%m.%Y")
print(birthday)

#-------------------------------------------------------------

if dayB > today:
    diff = birthday - today
    print(f"do urodzin zostalo: {diff}")
else:
    diff = dayB - today
    print(f"Urodziny byly dni temu: {diff}")



# wiecej w dokumentacji

