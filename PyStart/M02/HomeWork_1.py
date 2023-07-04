text = "Hello World"
counter = {}

for char in text:
    if char not in counter:
        counter[char] = 0
    counter[char] += 1
print(counter)
