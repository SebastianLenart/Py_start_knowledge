cities = ('Gdynia',) # przecinek powoduje ze to jest tuple
numbers = tuple(range(1, 20, 2))
print(numbers)
print(numbers[1:10:3]) # krok o 3
print(numbers[1:10:2])

examples = 'a', 'b', 'c', 'asdfwefrf'
print(max(examples)) # c, patrzy na 1szy znak

examples = 'a', 'b', 'c', 'cadfwefrf'
print(max(examples)) # cadfwefrf, patrzy na 2gi znak
print("------------------------------------------------------------")

names = "Seba", "Emczi", "Ula"
firstName, middleName, _ = names
print(firstName, middleName, _)
print("------------------------------------------------------------")
text = "I love Poland"
if "loves" in text:
    print("jest")
else:
    print("nie jest")
