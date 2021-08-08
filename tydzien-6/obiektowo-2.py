'''
class NameClass:
    def __init__(self, ..., ):

    def NazwaMetodyDostepuDoZmiennych:
        return wartosc
'''


import random
from time import sleep


class Wojownik():
    def __init__(self, imie, zycie, pAtaku, pObrony):
        self.pObrony = pObrony
        self.pAtaku = pAtaku
        self.zycie = zycie
        self.imie = imie

    def atak(self):
        return random.randint(0, self.pAtaku)

    def obrona(self):
        return random.randint(0, self.pObrony)

    def straconeZycie(self, ilosc):
        self.zycie -= ilosc
        if self.zycie <= 0:
            print("koniec zycia ", self.imie)

    def czyZywy(self):
        if self.zycie <=0:
            return False
        else:
            return True

    def __str__(self):
        return self.imie

def walka(malpa, rycerz):
    i = 1
    while (malpa.czyZywy() and rycerz.czyZywy()):
        print('Runda nr: ', i)
        wyswietlStraty(malpa, rycerz)

        if random.randint(0, 1) == 0:
            pojedynek(malpa,rycerz)
        else:
            pojedynek(rycerz, malpa)

        print('')
        sleep(1)
        i += 1

    if rycerz.czyZywy():
        print(' wygral rycerz')
    else:
        print('wygrała małpa')

def pojedynek(x,y):
    print(x, ' zatakowany przez ', y)
    obrazenia = y.atak() - x.obrona()
    print(x, 'stracil ', obrazenia, ' punktow zycia')
    x.straconeZycie(obrazenia)

def wyswietlStraty(x,y):
    for i in (x,y):
        pass
    print(i, 'ma', i.zycie, 'punktow zycia')

rycerz = Wojownik('rycerz', random.randint(100,1000), random.randint(10, 50), random.randint(5,30))
malpa = Wojownik('malpa', random.randint(100,1000), random.randint(10, 50), random.randint(5,30))

walka(malpa, rycerz)

