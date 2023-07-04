text = "raz raz raz dwa dwa trzy"
textList = text.split(" ")
counter = {}

for word in textList:
    if word not in counter:
        counter[word] = 0 # zeby zawsze byl klucz, odwolanie
    counter[word] += 1
print(counter)