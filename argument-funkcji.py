def cos(a, b, *args):
    print('a= ', a)
    print('b= ', b)
    print(args)
    print(*args)


print(cos(1, 2, 9, 9, 9))


def log(*args, **kwargs):
    print(args)
    print(kwargs)


log(1, 2, 3, hello='ktos', imie='imie')

def get_brutto(netto, vat):
    return netto + netto * vat

values = [
    (100, 0.23),
    (50, 0.05)
]

for value in values:
    print(get_brutto(*value))

