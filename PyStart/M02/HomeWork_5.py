word1 = input("Podaj 1sze slowo: ")

# word1 = ''.join(word1.split('')) # bez spacji

if word1 == word1[::-1]:
    print("To sa palindromy")
else:
    print("to nie sa palindromy")

print(word1)
print(word1[::-1])  # odwraca kolejnosc!!!
