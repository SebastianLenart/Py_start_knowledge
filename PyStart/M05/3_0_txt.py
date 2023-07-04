result = []
with open("sample.txt") as input_file:
    for line in input_file:
        number = int(line.strip())
        if number % 2 == 0:
            result.append(number)


print(result)

with open("even.txt", "w") as output_file:
    for number in result:
        output_file.write(f"{number}\n")

