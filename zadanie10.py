# value = [1, 4, 5, 6, 8, 10, 11, 12, 14, 17, 19, 20, 22, 23, 24]
# value = list(range(1, 101)) #inna inicjacja list wartościami :-)
# numbres_division_4 = 0
# numbres_division_5 = 0
#
# for numer in value:
#     if numer % 5 ==0:
#         numbres_division_5 +=1
#
#     if numer % 4 == 0:
#         numbres_division_4 +=1
#
# print(f'podzielne przez 4:  {numbres_division_4}')
# print(f'podzielne przez 5:  {numbres_division_5}')
#
#
# names = ['aga', 'alek', 'olga', 'piotr', 'janusz', 'gerwazy']
# shortest_names = None
# longest_names = None
#
# for name in names:
#     if shortest_names is None or len(name) < len(shortest_names):
#         shortest_names = name
#
#     if longest_names is None or len(name) > len(longest_names):
#         longest_names = name
#
# print(f'najkrotsze imie: {shortest_names}')
# print(f'najdłuższe imię: {longest_names}')


b = int(input('podaj liczbę do wyświetlenia'))

for i in range(0, b+1):
    print('')
    for x in range(1, b+1):
        print(x, end=' ')
    b -= 1

