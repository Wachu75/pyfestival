# pesel = input('podaj pesel: ')
# if len(pesel) > 11:
#     quit()
# pesel = list(pesel)
pesel = '18210177915'
mnoznik = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
#pesel = list(pesel)
temp = list(zip(pesel,mnoznik))

print(temp)
suma = 0
for pesel, mnoznik in zip(pesel,mnoznik):
    suma = suma + (int(pesel) * int(mnoznik))

print(suma)

if str(suma)[-1] == '0':
    print('pesel jest prawidłowy')
else:
    print('pesel nieprawidlowy')