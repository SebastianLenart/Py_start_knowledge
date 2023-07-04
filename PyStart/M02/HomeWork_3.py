"""
ord - znak na ASCII
chr - ASCII na znak
a->d
b->e
..
z->c

"""
text = input("Podaj tekst do odszyfrowania lub zaszyfrowania: ")
option = input("1-szyfruj, 2 deszyfruj")

if option == "1":
    result = ""
    for char in text:
        if ord(char) >= ord('x'):
            result += chr(ord(char) - 23)
        else:
            result += chr(ord(char) + 3)  # zawsze o 3 chyba
    print(result)

elif option == "2":
    result = ""
    for char in text:
        if ord(char) >= ord('d') or char == '#': # szyfr Cezara, spacja -> + 3 = #
            result += chr(ord(char) - 3)
        else:
            result += chr(ord(char) + 23)
    print(result)
else:
    print("Nie wiem co wybrac")
