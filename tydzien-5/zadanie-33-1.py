from json import load, dump

try:
    with open('books.json') as file:
        books = load(file)
except FileNotFoundError:
    books = []

choice = input('[w]ypisz  , [d]odaj:')

if choice == 'w':
    for book in books:
        print(f"- {book['autor']} {book['title']}")
elif choice == 'd':
    author = input('imie nazwisko autora:')
    title = input('podaj tytuł:')

    books.append({
        'autor': author,
        'title': title
    })
    with open('books.json', 'w') as file:
        dump(books, file)

else:
    print("nie rozumiem")
