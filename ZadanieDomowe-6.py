from math import sqrt

def czy_pierwsza(n,m):
    #print(f'n: {n}, m: {m}')
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    pierwsza = int((sqrt(n) + 1))
    #print(f'zm.pierwsza= {pierwsza}')
    # if m <= 1:
    #     m = 2
    for dzielnik in range(2, pierwsza + 1):
        #print(f'zm.dzielnik w for: {dzielnik}')
        if n % dzielnik == 0:
        #print(f'zm.n%dzielnik= {(n % dzielnik)}')
            return False
    return True

min = int(input('podaj najmniejszą liczbę > 0: '))
max = int(input('podaj najwiekszą liczbę: '))

for i in range(min,max+1):
    if czy_pierwsza(i,min) == True:
        print(f'liczba pierwsza:  {i}')
    # else:
    #     print(f'liczba: {i}, nie jest liczbą pierwszą')

# rozwiązanie Kacpra

# bardzo podobne




