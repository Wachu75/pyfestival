import sqlite3

#connection = sqlite3.connect('library.db')
#connection.close()

with sqlite3.connect('library.db') as connection:
    cursor = connection.cursor()
    books = cursor.execute('SELECT book_id, title, author')
    #pobieramy od urzytkownika i wpisujemy do bazy
    title = input('tytuł:')
    author = input('autor: ')
    cursor.execute('INSERT INTO books VALUES (null, ?, ?)',(title, author))
    connection.commit()

    # CREATE TABLE books(
    #     book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     title VARCHAR(100) UNIQUE NOT NULL,
    #     autor VARCHAR(100)
    # )

