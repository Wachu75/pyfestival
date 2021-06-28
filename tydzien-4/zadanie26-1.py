from functools import reduce
from math import sqrt

values = [1,2,3,4,5,6,7,8,9,10,16,25,36,49]
# reduce()
#even = lambda x: sqrt(x) if x % 2 == 0
filtered2 = [n for n in values if n % 2 == 0]           #przy użyciu listcomperhesion
filtered = filter(lambda n: sqrt(n) % 2 == 0, values)   #przy urzyciu funkcje + lambda
filtered3 = map(sqrt, values)
print(list(filtered))
print(list(filtered3))
numbers = [
    (1, 2),
    (3, 4),
    (5, 6)
]
total = sum([a*b for a, b in numbers])
print(total)

total1 = reduce(lambda sum, a: sum + a[0] * a[1], numbers, 0)
# 0 na koncu służy do zainicjowania poczatkowej wartosci sum ponieważ na początku ma wartość none i trzeba to jakoś obsłużyc
print(total1)

name = ['ala nowak', 'monika dZIecioł', 'jacek kulAwy', 'wieslaw zmrozony', 'krzysztof ogrodnik', 'wrona ala']
# by_alphabet = sorted(name)
# print(by_alphabet)
# by_last_letter = sorted(name, key=lambda x: x[-1])
# print(by_last_letter)
names2 = name[0].split(' ')
names2 = names2[1].title()
print(type(names2))
names3 = [name[n].title().split(' ') for n, names in enumerate(name)]
names4 = sorted(names3, key=lambda x: x[1])
#names3 = str(names3)
print(type(names3))
#names4 = [names3[n].title() for n in enumerate(names3)]
#print(type(names2))
print(names2)

print(names3)

print(names4)

# rozwiazaanie Kacpra

