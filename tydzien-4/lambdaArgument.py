from collections.abc import Callable

# callable[[argument_type], return_type]

def do_something(data: list, f: Callable[[list], int]):
    return f(data)

print(do_something([1,2,3], sum))
print(do_something([4,5,6], len))

def total_salary(base, extra):
    return base + extra(base)

def calculate_extra(amount):
    return 0.1 * amount

print(total_salary(1000,calculate_extra)) # funkcje przekazujemy bez nawiasów () czyli nie jako wywołanie tylko jako sposób

# teraz konkret na temat lambda czyli aby uprościć to co wyżej ( przekazanie funkcji)
# lambda arg1, arg2, arg : arg1 + arg2 + arg
# kolejne argumenty przekazujemy po przecinku
# kilka przyddatnych funkcji
# filter - usuwa elementy
# Map   - zamienia elementy
# Reduce    - redukuje elementy
# sorted    - funkcje sortujące
# function_name(callback, iterable) callback funkcja do zastosowania na elementach iterable - lista, słownik na którym chcemy działać

numbers = [1,2,3,4,5]

doubles = map(lambda n: n+n, numbers) # na każdym elemencie n wykona się n+n na numbers
filtered = filter(lambda n: n % 2 == 0, numbers) # zwróci tylko te wartości dla których wyrażenie jest prawdziwe

from functools import reduce
numbers = [
    (1, 2),
    (3, 4),
    (5, 6)
]
# chcąc policzyć sumę iloczynów
total = sum([a*b for a,b in numbers]) #
print(total)
total1 = reduce(lambda sum, a: sum + a[0] * a[1], numbers, 0)
print(total1)
# reduce musimy zaimportować reduce(funkcja lambda, po czym iterujemy , wartość początkowa) !!!
# zmienna sum będzie w pierwszym wywołaniu funkcji reduce wartość początkową 0 do którego doda iloczyn a[0]*a[1]
# jeżeli nie podamy wartości początkowej to przyjmuje ona wartość None z którym musimu sobie jakoś poradzić i obsłużyć
#
# co lepsze list comprehension czy funkcje+lambda
# to co bardzej mi pasuje

