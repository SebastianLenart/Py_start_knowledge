summary = 0
with open("income.csv", "r", encoding="utf-8") as handler:
    for line in handler:
        line_arr = line.strip().split(",")
        created_at, description, value = line_arr
        summary += int(value)
print(summary)






















