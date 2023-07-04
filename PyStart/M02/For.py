books = ['Krzyzacy','Turbulencja','Potop']

# print(dir(enumerate))
print( "--------")
# print(help(enumerate))

# enumerate robi w krotke

for book in enumerate(reversed(books), start=1): # zamiast reversed moze byc sorted
    print(book)
    print(book[0])

print( "--------")

for id, book in enumerate(reversed(books), start=1): # zamiast reversed moze byc sorted
    print(id, book)