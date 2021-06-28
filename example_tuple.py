'''
tupla/krotka jest niemutowalna tzn nie możemy jej zmieniać
tupla jezeli ma jeden element to musi mieć przecinek po pierwszym elemencie , bez przecinka jest to string!
operator zakresu przeszukiwania iteracji [ początek : koniec : skok ] brak wartości czyli tylko : oznacza wszystko
do rzutowania innego typu na tuple urzywamy tuple(typ)
name, _, surname = name1 -> podkreślenie _ urzywamy gdy musimy iterować ale nie potrzebujemy pobranej wartości
jeżeli nie dajemy nawiasów [ ] domyślnie definuijemy tuple ważne przy definiowaniu list
'''
name1 = 'Krzysztof', '123', 'Nazwisko'  # tupla
children = (1, 2, 4)                    # tupla
cities = ('Wrocław', )                    # tupla w definicji mamy przecinek za pierwszym elementem !
cities2 = "Poznan", "Wrocław", "Gdynia" # tupla
a = tuple(range(11))                    # tupla
innaTupla = (1, 'string', 3.14, True)
str1 = 'string'
print(str1)
tupla1 = tuple(str1)
print(tupla1)

print(a)
print(cities2[1])
print(a[::3])
print(a[-3:])
print(a[::-1])
b = len(cities2)        # podaje długość normalnie tzn 3
print(b)
c = max(children)
d = min(children)
e = sum(children)
print(e)
x = (1, 2, 3) * 3
print(x)
x *= 2
print(x)

names = 'cyprian', 'kamil', 'norwid'
first, _, last = names  # podkreslenie _ gdy musimy cos wyliczyć ale nie chcemy używać co nie zmienia możliwości użycia
print(first)
print(last)


