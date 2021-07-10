import random

list_tuple = []

def list_for_compute(value, range_value, random_values):
    for howMuch in range(0, value):
        listTemp = []
        for data in range(0, random.randint(1, range_value)):
            listTemp.append((random.randint(0, random_values)))
        list_tuple.append(tuple(listTemp))
    return list_tuple

print('Program liczy zawartość listy składającej się z tupli, \n'
      'każda tupla skłąda się z losowej liczby elementów od 1 do liczby podanej przez urzytkownika > 6\n')
value = int(input('Podaj ilość elementów listy: '))
random_values = int(input('Podaj górny zakes liczb do losowania występujących w tupli: '))
range_value = int(input('podaj górną wartość do losowania ilości elementów z których zbudowana jest tupla: '))


list_for_compute(value, range_value, random_values)

for x in list_tuple:
    print(x)

# krok pierwszy tzn. za pomocą pętli :-)
# for data in list_tuple:
#     if len(data) == 0 or (len(data) > 1 and len(data) < 7):
#         if len(data) % 2 == 0:
#             print(f'suma elementów tupli z przystą liczbą elementów:  {sum(data)}')
#         else:
#             print(f'średnia elementów tupli z nieparzystą liczbą elementów: {sum(data) / len(data)}')

for data in list_tuple:
    equal_sum = [sum(data) for data in list_tuple if (len(data) > 1 and len(data) < 7 and len(data) % 2 == 0)]
    equal_medium = [sum(data) / len(data) for data in list_tuple if (len(data) > 1 and len(data) < 7 and len(data) % 2 != 0)]
    monstrosity = [(sum(data) if (len(data) > 1 and len(data) < 7 and len(data) % 2 == 0) else (sum(data) / len(data)
                    if (len(data) > 1 and len(data) < 7 and len(data) % 2 != 0) else False)) for data in list_tuple]

print('-'*50)
print("drukuje kolejne wyniki z tupli w których ilość elementów była >1 <7")
print('-'*50)
print(f"suma gdy ilość elementów w tupli była parzysta:  {equal_sum}")
print('-'*50)
print(f"oraz średnia gdy ilość elementów tupli była nieparzysta {equal_medium}")
print('-'*50)
res = list(filter(None, monstrosity))
print(f"drukuje oba powyższe warunki w kolejności wystąpienia {res}")