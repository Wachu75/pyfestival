books = 'w pustyni i pusz', 'krzyzacy', 'potop'

for number, book in enumerate(books, start=1):
    print(book, number)
    print(number, book)

for book in enumerate(books, start=1):
    print(book)