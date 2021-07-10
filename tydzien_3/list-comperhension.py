# zastosowania

# budowanie listy mapowanie czyli zamiana jednych danych na inne
# filtrowanie danych
#
# na początek nawiasy kwadratowe mówią że tworzymy liste
print([n * 3 for n in range(1, 11)])
#-------------------------------------------------------
new_list = []
for n in range(1,11):
    if n % 2 == 0:
        new_list.append('even')
    else:
        new_list.append('odd')
#lub z urzyciem list comperhension skróciliśmy do 1 lini

new_list = ['even' if n % 2 == 0 else 'odd' for n in range(1, 11)]

print(new_list)
#-------------------------------------------------------
# filtrowanie

names = ['Janek', 'Inga', 'Krzysztof', 'Basia']
ladies = []
for name in names:
    if name[-1] == 'a':
        ladies.append(name)
# lub z urzyciem list comperhension
names = ['Janek', 'Inga', 'Krzysztof', 'Basia']
ladies = [name for name in names if name[-1] == 'a']
print(ladies)

#-------------------------------------------------------
# tworzymy litę TUPLI (...)-> person_2_in_1

persons = [
    ('Janek', 'wisnia', 'Gdynia'),
    ('Grzegorz', 'Turnał', 'Kraków'),
    ('sowa', 'winna', 'Warszawa'),
    ('misiek', 'ktosik', 'Grodno')
]
print(type(persons))
persons_g = [person for person in persons if person[-1][0] == 'G']
person_upp = [(person[0], person[1], person[2].upper()) for person in persons_g]
#print(persons_g)
#print(person_upp)

person_2_in_1 = [(p[0], p[1], p[2].upper()) for p in persons if p[-1][0] == 'G']
print(person_2_in_1)