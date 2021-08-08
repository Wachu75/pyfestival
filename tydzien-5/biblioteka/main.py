import sqlite3

def get_books(c):
    return c.execute('SELECT book_id, title, author FROM books')

def save_book(connec, tit, aut):
    c = connec.cursor()
    c.execute('INSERT INTO books(title, author) VALUES (?, ?)', (tit, aut))
    connec.commit()

action = input('co chcesz zrobić w-yswietl   d-odaj')

if action == 'w':
    with sqlite3.connect('library.db') as connection:
        cursor = connection.cursor()
        for book in get_books(cursor):
            print(book)
            book_id, title, author = book
            print(f'Id: {book_id}, Tytul: {title}, Autor {author}')

elif action == 'd':
    with sqlite3.connect('library.db') as connection:

        title = input('tytul ')
        author = input('autor: ')
        save_book(connection, title, author)
        # cursor = connection.cursor()
        # cursor.execute('INSTERT INTO books(title, author) VALUES (?, ?)', (title, author))
        # connection.commit()
else:
    print('blad')

