list1 = [1,3,7]
list2 = [4,2,0]

# suma 5, 5, 7

lista = list(zip(list1, list2))
print(lista)
suma = list1[0] + list2[0]
sumka = map(int, str(suma))
print(list(sumka))
print(list(str(suma)))
sumka1 = [int(x) for x in str(suma)]
print(sumka1)

zsumowane = [x+y for x, y in zip(list1,list2)]
print(zsumowane)

def get_sum(list1: list, list2: list) -> list:
    total = []
    for a, b in zip(list1, list2):
        total.append(a + b)

    return total

    # return [a+b for a, b in zip(list1, list2)]
print(get_sum([1,2,3], [4,5,6]))
