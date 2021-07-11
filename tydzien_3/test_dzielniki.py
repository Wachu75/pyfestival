import math


def nwdzielnik(a, b):
    while (b != 0):
        c = a % b
        a = b
        b = c
    return a


def DzielnikiNiewlasciwe(a):
    wynik = []
    x = 0
    for i in range(1, int(math.sqrt(a)) + 1):
        if (a % i == 0):
            wynik.append(i)
            print('wynik[i]: ', wynik[x])
            x += 1
    #print('len(wynik)-1', len(wynik)-1)
    for i in range(len(wynik) - 1, -1, -1):
        print(wynik[i])
        if (a / wynik[i] != wynik[i]):
            wynik.append(a // wynik[i])
    return wynik


def DzielnikiLiczb(a, b):
    nwdziel = nwdzielnik(a, b)
    print(nwdziel)
    print('----------------------------')
    return DzielnikiNiewlasciwe(nwdziel)


a = int(input("Podaj dwie liczby:\n a = "))
b = int(input(" b = "))
dzielniki = DzielnikiLiczb(a, b)
print("Wspólne dzielniki liczb to:")
for x in dzielniki:
    print(x, end=" ")
