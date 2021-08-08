#
#
# class Autor:
#     def __init__(self, imie: str, nazwisko: str, data_urodzenia: str):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.data_urodzenia = data_urodzenia
#     def show_yourself(self):
#         return f"{self.imie},{self.nazwisko},{self.data_urodzenia}"
#
# class Ksiazka:
#     def __init__(self, tytul: str, gatunek: str, opis: str, streszczenie: str, ocena: float, autorzy: Autor):
#         self.tytul = tytul
#         self.gatunek = gatunek
#         self.opis = opis
#         self.streszenie = streszczenie
#         self.ocena = ocena
#         self.autorzy = autorzy
#
#     def show_ksiazka(self):
#         return f"{self.tytul}"
#         #return f'ksiazka z Ksiązka({self.tytul},{self.autorzy.show_yourself()},{self.opis})'
#
#     def get_info(self):
#         return f'{self.tytul}, {self.gatunek}'
#
#     def __str__(self):
#         return f'ksiazka z Ksiązka({self.tytul},{self.autorzy.show_yourself()},{self.opis})'
#
# class Dictionary:
#     def __init__(self):
#         self.ksiazkai = []
#
#     def add_new_book(self, ksiazka: Ksiazka):
#         self.ksiazkai.append(ksiazka)
#
#     def get_info_dictionary(self):
#         return self.ksiazkai # tu jest coś nie tak
#
#     def show_dictionary(self):
#         return f"{self.ksiazkai}"
#
#     def __str__(self):
#         return f'ksiazka z Dictionary ({self.ksiazkai})'
#
# book1 = Dictionary()
# book1.add_new_book(Ksiazka('W pustuni i puszczy','przygodowe','dla dzieci','o Stasiu i Nell',5,Autor('Bolesław','Prus','1980-05-05')))
# print(book1.ksiazkai[0])
# print(book1.ksiazkai)
# print(Ksiazka.show_ksiazka)
# # takie cos się wyświetla ???
# #print(book1.ksiazkai.__str__()) # a tutaj -> [<__main__.Ksiazka object at 0x0000019A16CB6BB0>]
# #print(book1.get_info_dictionary())

class Jablko:
    def __init__(self, kolor, smak, rodzaj):
        self.kolor = kolor
        self.smak = smak
        self.rodzaj = rodzaj

class Koszyk:
    def __init__(self):
        self.jablka = []

    def add(self, jablko: Jablko):
        self.jablka.append(jablko)



class Raport:
    def __init__(self, koszyk):
        self.koszyk = koszyk

    def raportuj(self):
        raport = {}
        for jablko in self.koszyk.jablka:
            if jablko.kolor not in raport:
                raport[jablko.kolor] = 0
            raport[jablko.kolor] += 1

        return raport


jablko1 = Jablko('czerwone', 'słodkie', 'dojrzale')
jablko2 = Jablko('czerwone', 'słodkie', 'niedojrzałe')
koszyk = Koszyk()

koszyk.add(jablko1)
koszyk.add(jablko2)

raport = Raport(koszyk)

dane = raport.raportuj()

print(koszyk)
print(dane)

#
# class A:
#     def __init__(self, val1: int, val2: int):
#         self.val1 = val1
#         self.val2 = val2
#
#     def showA(self):
#         return f"{self.val1}, {self.val2}"
#
# class B:
#     def __init__(self, val1: int, a: A):
#         self.val1 = val1
#         self.a = a
#
#     def showB(self):
#         return f"{self.val1}, {self.a.showA()}"
#
# newA = A(1,2)
# newB = B(3,newA)
#
#
# print(newA.showA())
# print(newB.showB())
