sentence = "12 kilogramow jablek, 10 kologramow gruszek, 20 kiligramow sliwek"
words = sentence.split(" ")

total = 0
for word in words:
    if word.isnumeric(): # sprawdza czy sa numery w tekscie
        total += int(word)
print(total)