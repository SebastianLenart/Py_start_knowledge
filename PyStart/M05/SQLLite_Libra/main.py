import sqlite3

def get_books(c):
    return c.execute("SELECT book_id, title, author FROM books")

def save_book(conn, t, a):
    c = conn.cursor()
    c.execute("INSERT INTO books(title, author) VALUES(?,?)", (t, a))
    conn.commit()

action = input("(W)yswietl, (D)odaj: ")
if action == "w":
    with sqlite3.connect('library.db') as connection:
        cursor = connection.cursor()
        for book in get_books(cursor):
            print(book) # jako tuple
            book_id, title, author = book
            print(f"id: {book_id}, Tytul: {title}, Author: {author}")

elif action == "d":
    with sqlite3.connect('library.db') as connection:
        cursor = connection.cursor()
        title = input("Tytul: ")
        author = input("Autor: ")
        save_book(connection, title, author)
else:
    print("Powtorz")