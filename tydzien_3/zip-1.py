zip1 = (1,2,3,4,5)
zip2 = (6,7,8,9,10)

print(list(zip(zip1, zip2)))

zip3 = ('a', 'b', 'c', 'd', 'e')

print(list(zip(zip3, zip2, zip1)))

first_names = ['Zofia', 'Leopold']
last_names = ['Nałkowska', 'Staff']

for first_names, last_names in zip(first_names,last_names):
    print(f'imie: {first_names}, nazwisko {last_names}')


