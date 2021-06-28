from datetime import datetime

class Autor:
    def __init__(self, first_name, last_name, date_birth_day):
        self.first_name = first_name
        self.last_name = last_name
        self.date_birth_day = date_birth_day

#
# class Autorzy:
#     def __init__(self, autor: Autor):
#         self.autor = autor


class Ksiazka:
    def __init__(self, tytul, gatunek, autor, opis, streszczenie, ocena):
        self.tytul = tytul
        self.gatunek = gatunek
        self.autor = autor
        self.opis = opis
        self.streszczenie = streszczenie
        self.ocena = ocena

bonifacy = Autor('bonifacy', 'iinu', datetime(1919,10,10))

ksiazka = Ksiazka(
    'przykladowy tytuł',
    'kryminaL',
    [bonifacy],
    'opis1',
    'krotkie streszenie',
    'oceniam na 3'
)


