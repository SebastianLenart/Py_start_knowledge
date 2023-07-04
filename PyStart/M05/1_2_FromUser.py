from datetime import datetime
birthday = input("Podaj date urodzenia dd.mm.rrrr")
d = datetime.strptime(birthday, "%d.%m.%Y") # tu jest p a nie f !!! 
print(d)