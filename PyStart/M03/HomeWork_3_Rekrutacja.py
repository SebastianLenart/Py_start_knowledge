def count_vowels(text):
    return sum([1 if char in "ąęśćźżńóaeyoui" else 0 for char in text])


print(count_vowels("programowanie"))
