"""
ANAGRAMY

ta sama dlugosc i te same wystepujace litery:
dzielenia
niedziela

"""

# najłatwiej posortowac XDDDD

word1 = input("Podaj 1sze slowo: ")
word2 = input("Podaj 2gie slowo: ")

if sorted(word1) == sorted(word2):
    print("To sa anagramy")
else:
    print("To NIE sa anagramy")
