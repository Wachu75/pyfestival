dictionary = dict.fromkeys(range(1,27),0)

dictionary1 = dict.fromkeys(range(27,53),0)

for key, values in dictionary.items():
    dictionary[key] = chr(int(key+64))

for key, values in dictionary1.items():
    dictionary1[key] = chr(int(key+70))

z = dict(dictionary | dictionary1)
z1 = {0: ' '}
z2 = dict(z1 | z)

tekstDoZaszyfrowania = input('podaj tekst do zaszyfrowania: ')
# pobierz pierwszą literę tekstu i porównaj z zawartością słownika z2 następnie pobierz key tej litery i dodaj +x x-wartość szyfru
szyfr = []
#print(type(szyfr))
key_list = list(z2.keys())
val_list = list(z2.values())
print(key_list)
print("-"*50)
print(val_list)
print('-'*50)
for i in tekstDoZaszyfrowania:
    #print(i)
    if i in val_list:
        #print(i)
        position = val_list.index(i)
        #print(key_list[position])
        #k = key_list[position]
        #print(type(key_list[position]))
        if key_list[position] > 52:
            key_list[position] -= 52
        else:
            key_list[position] += 3
    #print(type(key_list[position]))
    a = key_list[position]
    print(a)
    #letter = val_list.index(a)
    szyfr.append(val_list[a])
print(szyfr)

## wersja Kacpra

text= input('tekst do zaszyf')
option = input('1-odszyfrujj 2- zasz')

if option == '1':
    result = ''
    for char in text:
        if ord(char) >= ord('x'):
            result += char(ord(char) - 23)
        else:
            result += char(ord(char) + 3)
    print(result)
elif option == '2':
    result = ''
    for char in text:
        if ord(char) >= ord('d') or char == '#':
            result += char(ord(char) - 3)
        else:
            result += char(ord(char) + 23)
    print(result)
else:
    print('nie rozumiem')
     