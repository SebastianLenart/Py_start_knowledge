# 1 sposob
"""
from csv import reader, writer

# https://docs.python.org/3/library/csv.html
result = []
with open("tranzakcja.csv", encoding="utf-8") as input_file:
    content = reader(input_file, delimiter=",")  # aby byla lista
    next(content)
    for line in content:
        created_at, description, value = line
        if int(value) > 0:
            result.append(line)

with open("income.csv", "w", encoding="utf-8", newline="") as output_file:
    content = writer(output_file, delimiter=",")
    for line in result:
        content.writerow(line)

"""
# 2 sposob
result = []
with open("tranzakcja.csv", encoding="utf-8") as input_file:
    next(input_file)
    for line in input_file:
        line_as_list = line.strip().split(",")
        created_at, description, value = line_as_list
        if int(value) > 0:
            result.append(line)

print(result)


with open("income.csv", "w", encoding="utf-8", newline="") as output_file:
    output_file.writelines(result)









