imie = input('podaj imie: ')
if imie[len(imie)-1] == 'a':  #imie[-1] == 'a'
    print('pani')
else:
    print('pan')

for i in range(len(imie)):
    # print(i)
    # print(imie[i])
    if imie[i] == 'a':
        if i == 0:
            imie = "@" + imie[1:]
        elif i < len(imie):
            imie = imie[:i] + "@" + imie[i+1:]
    if imie[i] == 's':
        if i == 0:
            imie = "$" + imie[1:]
        elif i < len(imie):
            imie = imie[:i] + "$" + imie[i+1:]

imie = imie.replace('a', '@')
imie = imie.replace('s', '$')

        #print(imie[i])
        #imie[i] = '@'

#imie1 = "@" + imie[1:]
print(imie)

zdanie = 'Pies to najlepszy przyjaciel człowieka, lecz nie każdy pies o tym wie, że jest pies i '
zdanie = zdanie.lower()
print(zdanie.count('pies'))

zdanie2 = ' 12 kilogramow jablek, 10 kg gruszek, 20 kg śliwek'
zdanie2a = zdanie2.split(' ')
print(zdanie2a)
wynik = 0
for i in range(len(zdanie2a)):
    if zdanie2a[i].isdigit() == True:
        wynik += float(zdanie2a[i])
    # if isinstance(float(zdanie2a[i]), (float, int)):
    #     wynik += float(zdanie2a[i])

print(wynik)
# waga = 0
# for i in zdanie2a:
#     if i.isnumeric():
#         waga += int(i)
#
#print(f'waga: {waga}')

