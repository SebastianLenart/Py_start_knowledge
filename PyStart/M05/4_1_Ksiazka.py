from json import load, dump


try:
    with open("books.json") as file:
        books = load(file)
except FileNotFoundError:
    books = []


choice = input("(W)ypisz/(D)odaj: ")
if choice == "w":
    for book in books:
        print(f'Autor-{book["author"]}, tytul-{book["title"]}, ilosc stron: {book["pages"]}')
elif choice == "d":
    author = input("Imie i nazwisko autora: ")
    title = input("Podaj tytul: ")
    pages = input("Ilosc stron: ")

    books.append({
        'author': author,
        'title': title,
        'pages': pages,
    })
    with open("books.json", "w") as file:
        dump(books, file)
