

class Library:
    def __init__(self):
        self.book = []


class Author:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Book:
    def __init__(self, title, author: Author): # podajemy typ przekazywanej informacji
        self.title = title
        self.author = author


class Student:
    def __init__(self, first_name: str, last_name, week, age): # przy urzyciu ALT + ENTER możemy wybrać autouzupełnienie
        self.age = age                      # tych linijek !!!!
        self.week = week
        self.last_name = last_name
        self.first_name = first_name