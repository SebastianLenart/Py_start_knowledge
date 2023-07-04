def filter_vowels1(word):
    vowels = set()
    for letter in word:
        if letter in 'aeiouy':
            vowels.add(letter)
    return vowels


# ----------------------------------------------------------------
def filter_vowels2(word):
    return {c for c in word if c in "aeiouy"}


print(filter_vowels1("wercweqcrweriou"))
print(filter_vowels2("wercweqcrweriou"))

# ----------------------------------------------------------------
from math import sqrt, floor


def is_prime(number):
    for div in range(2, floor(sqrt(number)) + 1):
        if number % div == 0:
            return False
    return True

print(9, is_prime(9))
print(11, is_prime(11))
