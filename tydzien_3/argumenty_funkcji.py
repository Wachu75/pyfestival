#  argumenty nazwane funkcji podajemy po argumentach nienazwanych
#  argumenty pozycyjne muszą być przed nazwanymi
#  w wywołąniu funkcji możemy używać nazw argumentów w ten sposób łatwiej jest rozkminić czego dotyczy przekazywany argument
#  pierwszy argument nienazwany przekazywany w funkcji idzie jako pierwszy w funkcji resztą możemy już dowolnie
#  manipulować
#  stosując argumenty nazwane mogą być w dowolnej kolejnośći ale lepiej dla czytelności kodu
#  zachować kolejność w definicji funkcji
# def zrob_cos(a=1, b=1):
#     return a * b
#
# print(zrob_cos(2,3))
from typing import Union


def find_divisors(a):
    # divisors = set()
    # for divisor in range(2, a+1):
    #     if a % divisor == 0:
    #         divisors.add(divisor)
    # return divisors
    return {divisor for divisor in range(2, a + 1) if a % divisor == 0}


def calculate_common_divisor(a, b, offset=2):
    common_divisors = find_divisors(a) & find_divisors(b)
    common_divisors = [divisor for divisor in common_divisors if divisor >= offset]
    return (sorted(list(common_divisors))) if len(common_divisors) > 0 else None


test1 = calculate_common_divisor(4, 14)
print(test1)

test1 = calculate_common_divisor(3, 6, offset=4) # podaliśmy nazwę argumentu w wywołaniu funkcji !
print(test1)

test1 = calculate_common_divisor(b=4, a=12)
print(test1)


def cos(a, b, c=10) -> int:
    return a * b * c


print(cos(10, b=2, c=3))

print(cos(10, c=3, b=2))


def argument_type(netto: int = 1, vat: float = 1):  # argumenty mogą mieć typ domyślny który widzimy w trakcie pisania kodu
    return netto * vat


print(argument_type(12.3, 1.23))

def age(age: int) -> bool:  # możemy również podać typ zwracany przez funkcję
    return age >= 18

print(age(19))

def argumenty(something: Union[int, str]): # argument może być typu union czyli dowolny z wymienionych [...]
    print(something)

argumenty('Kamil')
argumenty(123)

def get_car_details():  # czasami gdy chcemy aby funkcja zwróciła więcej niż jeden argument
                        # może być zwrócony słownik lub listę słowników czyli typy złożone
    return {
        'r': 'a',
        'm': 'b',
        'n': 'qqqq'
    }

def get_car_size():    # po przecinakch j/n czyli zwracamy tuple
    a = 19999
    b = 2
    c = 4
    return a, b, c

zmienna1, zmienna2, zmienna3 = get_car_size()  # zmienna1 otrzyma a zmienna2 = b zmienna3 = c

print(zmienna1)
