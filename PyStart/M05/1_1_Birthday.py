from datetime import date, timedelta, datetime

today = date.today()
birthday = date(today.year, month=2, day=24)

if today > birthday:
    birthday = date(today.year+1, 2, 24)
# else:
diff = birthday - today
print(f"Urodziny za {diff.days}")
print(f"Bedzie to dzien {birthday.strftime('%A')}")
print("-"*10)

#--------------------------------------------------------------

for year in range(1998, 2030):
    bithday = date(year, month=2, day=24)
    print(f"W roku {year} to byl {bithday.strftime('%A')}")
print("-"*10)

#--------------------------------------------------------------

start = today
diff = timedelta(days=7)
end = start + diff # nie mozna start + 7
print(end.strftime("%d.%m.%y"))
print("-"*10)

#--------------------------------------------------------------
# czas a nie data teraz

event = datetime.today()
print(event.strftime("%H.%M.%S"))
















