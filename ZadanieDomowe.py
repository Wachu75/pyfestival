longstring = input('podaj dowolny napis:')

longstring = longstring.replace(' ', '')

# longstring = (' '.join(longstring))

counter = {}

for word in longstring:
    if word not in counter:
        counter[word] = 0  # w tym miejscu tworzymy według klucza word nową wartość = 0 ponieważ linię niżej zwiększamy ją do 1
                            # jest to zabezpieczenie aby nie powielać if'ów i nie kombinować z iteracjami
    counter[word] += 1      # tu dodajemy właścią iterację wartości o ile word w słowniku jest nową wartością

print(counter)

## wersja Kacpra

