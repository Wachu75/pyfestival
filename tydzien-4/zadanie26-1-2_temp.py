from functools import reduce
from math import sqrt

values = [1,2,3,4,5,6,7,8,9,10,16,25,36,49]
# reduce()
#even = lambda x: sqrt(x) if x % 2 == 0
filtered2 = [n for n in values if sqrt(n) % 2 == 0]           #przy użyciu listcomperhesion
filtered = filter(lambda n: sqrt(n) % 2 == 0, values)   #przy urzyciu funkcje + lambda
filtered3 = map(sqrt, values)
print(list(filtered2))
print(list(filtered))
print(list(filtered3))
print('-' * 50)
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
print('-' * 50)
name = ['ala nowak', 'monika dZIeciołp', 'jacek kulAwyr', 'wieslaw zmrozony', 'krzysztof ogrodnik', 'alA wroNa']

# by_alphabet = sorted(name)
# print(by_alphabet)
# by_last_letter = sorted(name, key=lambda x: x[-1]) # do kwarka key możemy przekkazać lambde i sortować po ostatniej literze
# print(by_last_letter)
# by_length = sorted(name, key=len)
names2 = name[0].split(' ') #.split(' ') rozbija string po spacjach i zwraca liste
names2 = names2[1].title()
names3 = [name[n].title() for n, names in enumerate(name)]
names5 = [name[n].title().split(' ') for n, names in enumerate(name)]
names4 = sorted(names3, key=lambda x: x[-1])   # nie działa prawidłowo na polskich literach jak było ostatnie ł w
# nazwisku to wywaliło na koniec listy !? czy ja czgoś tu nie rozumiem - do sprawdzenia
name_test = ['a a', 'b f', 'n ł', 'x ą', 'q w', 'a z', 'c v', 'x ź', 'ó ń', 'ą ę']
names_test = [name_test[n].title() for n, names in enumerate(name_test)]
names_test = sorted(names_test, key=lambda x: x[0])
names_test1 = sorted(names_test, key=lambda x: x[-1])
print(names_test)
print(names_test1)
print('-' * 50)
#names4 = [names3[n].title() for n in enumerate(names3)]
#print(type(names2))
print(names2)
print(names3)
print(names4)
print(names5)
# rozwiazaanie Kacpra w innym pliku

