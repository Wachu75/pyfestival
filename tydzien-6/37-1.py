from datetime import datetime

class Autor:
    def __init__(self, first_name, last_name, date_birth_day):
        self.first_name = first_name
        self.last_name = last_name
        self.date_birth_day = date_birth_day
    def show_autor(self):
        return f'{self.first_name},{self.last_name}'

class Autorzy:
    def __init__(self):
         self.lista_autorow = []

    def add(self, autor: Autor):
         self.lista_autorow.append(autor)


class Ksiazka:
    def __init__(self, tytul, gatunek, autor: Autorzy, opis, streszczenie, ocena):
        self.tytul = tytul
        self.gatunek = gatunek
        self.autor = autor
        self.opis = opis
        self.streszczenie = streszczenie
        self.ocena = ocena

    def show(self):
        return f'{self.tytul},{self.autor[1].show_autor()}'
        #print(self.autor(Autor.show_autor(self)))

bonifacy = Autor('bonifacy', 'ambroży', datetime(1919,10,10))
jon = Autor('jon','smith', datetime(1905,10,1))
ksiazka = Ksiazka(
    'przykladowy tytuł',
    'kryminaL',
    [bonifacy,jon],
    'opis1',
    'krotkie streszenie',
    'oceniam na 3'
)


#print(Autor.show_autor(bonifacy))
print(ksiazka.show())
print(ksiazka.autor[1])