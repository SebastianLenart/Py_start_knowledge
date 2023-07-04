names = ["Leon", "Barbara", "Czeslaw", "Fryderyk"]

by_alphabet = sorted(names)
print("alfa:",by_alphabet)

by_last_letter = sorted(names, key=lambda x: x[-1])
print("ost. litera:", by_last_letter)

by_length = sorted(names, key=len, reverse=True)
print("len:", by_length)

#--- powtorka ---
print(list(reversed(sorted([1, 2, 3]))))


"""
List comprehension vs funkcje lambda 

"""

