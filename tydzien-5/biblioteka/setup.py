import sqlite3

with sqlite3.connect('library.db') as connection:
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE books (book_id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR(100) UNIQUE NOT NULL, author VARCHAR(100))')
    connection.commit()

# w readme.nd jest informacja o tym co musimy zrobić i w pierwszej kolejności uruchamiamy setup.py
# setup.py tworzy baze danych
# cursor to takie kursor łączący z bazą danych taki wskaźnik
# cursor.execute wykonaj na cursor który jest połączony z bazą
#  !!! jak mamy dłuższe wywołanie sql to możemy użyć  '''    sql     '''  i napisać to w kilku linijkach
# ('''CREATE TABLE books (
# book_id INTEGER PRIMARY KEY AUTOINCREMENT,
# title VARCHAR(100) UNIQUE NOT NULL,
# author VARCHAR(100))''')