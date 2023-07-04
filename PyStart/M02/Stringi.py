text = "Hello, Word"

for char in text:
    print(char)

print(list(reversed(text)))
print(("He" in text))
print(text.replace("He", "Hi"))
print(text.find("o")) # podobne do lini 7 \
print("-------------")

# laczenie
person = ["Zofia", "Nalkowska"]
print("--".join(person))