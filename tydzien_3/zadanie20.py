from math import sqrt


def calculate_common_divisior_1(a, b):
    while (b != 0):
        c = a % b
        a = b
        b = c
    return a


def calculate_common_divisior(a, c=1):
    wynik = []
    wynik1 = []
    for i in range(2, int(sqrt(a)) + 1):
        if (a % i == 0):
            wynik.append(i)
    for i in range(len(wynik) - 1, -1, -1):
        print(i)
        if (a / wynik[i] != wynik[i]):
            wynik.append(a // wynik[i])
    print('len(wynik)', len(wynik))
    for i in range(len(wynik)):
        if c <= wynik[i]: wynik1.append(wynik[i])
    if len(wynik1) > 0:
        return wynik1
    else:
        return None


a = int(input("Podaj dwie liczby:\n a = "))
b = int(input(" b = "))
c = int(input('podaj wartość początkową od której wyświetlone będą dzielniki: '))
dzielniki = calculate_common_divisior_1(a, b)
wspolnedzielniki = calculate_common_divisior(dzielniki, c)
print("Wspólne dzielniki liczb to:")

if wspolnedzielniki == None:
    print('None')
else:
    for x in wspolnedzielniki:
        print(x, end=" ")
