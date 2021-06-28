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

test1 = calculate_common_divisor(3, 6, offset=4)
print(test1)

test1 = calculate_common_divisor(b=4, a=12)
print(test1)


def cos(a, b, c=10) -> int:
    return a * b * c


print(cos(10, b=2, c=3))

print(cos(10, c=3, b=2))


def argument_type(netto: int = 1, vat: float = 1):
    return netto * vat


print(argument_type(12.3, 1.23))

def age(age: int) -> bool:
    return age >= 18

print(age(19))

def argumenty(something: Union[int, str]):
    print(something)

argumenty('Kamil')
argumenty(123)

def get_car_details():
    return {
        'r': 'a',
        'm': 'b',
        'n': 'qqqq'
    }

def get_car_size():
    a = 19999
    b = 2
    c = 4
    return a, b, c

zmienna1, zmienna2, zmienna3 = get_car_size()

print(zmienna1)
