from math import floor

def isItPrime(n):
    if n == 1: return True
    is_prime = True
    for value in range(2,floor(n**0.5)+1):
        if n % value == 0:
            return False

    return True

value = int(input('podaj liczbę do sprawdzenia czy jest pierwsza: '))

print(isItPrime(value))
