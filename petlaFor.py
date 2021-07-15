fruits = ['owoc', 'aple', 'lemon', 'aple']
list(fruits)

for frut in fruits:  # wydrukuje kolejne elementy listy
    print(frut)

for frut in fruits: # wydrukuje całą listę tyle razy ile jest elementów w literowanym elemencie
    print(fruits)

print('-'*100)
# b = len(fruits)
# print(b)
for frut in range(len(fruits)):
    print(frut, fruits[frut])  #nada frut kolejne wartości indexu i wydrukuje kolejne elementy listy
    print(len(fruits[frut]))   #wydrukuje długość słowa

print('-' * 100)

for frut in range(len(fruits)):
    print(fruits)               #wydrukuje całą zawartość listy fruits tyle razy ile wynosi len(jakas_zmienna)

for i in range(1,21,2):
    print(i)


