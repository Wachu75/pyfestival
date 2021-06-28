books = ['w pustyni i w puszczy', 'krzyżacy', 'lalka']

for number, book in enumerate(books, start=1):
    print(number, book)

for book in enumerate(books):
    print(book)     # rzutuje na tuple/krotke

