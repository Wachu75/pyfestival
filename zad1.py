lista = []

for it in range(1, 5):
    value = int(input('podaj liczbe: '))
    lista.append(value)

print(lista)
print(sum(lista))


lista.remove(lista[2])

print(lista)
