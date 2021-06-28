pesel = input('podaj pesel: ')
if len(pesel) > 11:
    quit()

mnoznik = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]

suma_kontrolna = 0

for i in range(len(pesel)):
    suma_kontrolna += (int(pesel[i]) * int(mnoznik[int(i)]))
    #print(f'suma_kontrolna: {suma_kontrolna}  ',end=' ')
    #print(f'mnoznik[int(i)]:{mnoznik[int(i)]}', end=', ')
    #print(f'pesel[i]: {pesel[i]}')

#print(suma_kontrolna)
#print(type(suma_kontrolna))
lastdigit = int(repr(suma_kontrolna)[-1])
print(lastdigit)
if lastdigit == 0:
    print('poprawny')
else:
    print('niepoprawny')

## wersja Kacpra

pesel = '18210177915'
check = '13791379131'
control = 0
for index, _ in enumerate(pesel):
    control += int(pesel[index]) * int(check[index])
if str(control)[-1] == '0':
    print('pesel jest prawidłowy')
else:
    print('pesel nieprawidlowy')
