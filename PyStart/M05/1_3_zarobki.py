from datetime import datetime, timedelta

start = input("podaj date rozpoczecia dd.mm.rrrr")
end = input("podaj date zakonczenia dd.mm.rrrr")
wage = int(input("podaj stawke dzienna"))

date_start = datetime.strptime(start, "%d.%m.%Y")
date_end = datetime.strptime(end, "%d.%m.%Y")
diff = date_end - date_start
working_days = diff.days + 1

project_day = date_start

for _ in range(0, working_days ):
    if project_day.strftime("%a") in ["Sat", "Sun"]:
        working_days += 1
    print(f"Pracujesz w {project_day.strftime('%a.%d.%m.%Y')}")
    project_day += timedelta(days=1)

print(f"zarobiono {working_days * wage}")
