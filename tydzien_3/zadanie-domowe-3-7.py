#Przygotuj funkcję która zwróci największy wspólny dzielnik dla dwóch liczb przekazanych w jej argumentach.

def NWD(a, b):
    while (b != 0):
        temp = b
        b = a % b
        a = temp
    return a

a = int(input('Podaj pierwszą liczbę: '))
b = int(input('Podaj drugą liczbę: '))

print(NWD(a,b))


