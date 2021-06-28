values = []
#temp = []
#ilosc = 0
#while ilosc < 1:
while len(values) < 10:
    value = int(input('podaj liczbę dodatnia: '))
    if value > 0:
        values.append(value)

print(min(values))
print(max(values))
#sorted(temp)
#print(temp[0])
#print(temp[-1])

value = 0
max = 0
temp = 0
ilosc = 0
is_not_max = False
while not is_not_max:
    value = int(input('podaj liczbę większą od ostatniej: '))
    if value < max:
        is_not_max = True
        break
    temp += value
    ilosc += 1
    max = value

# można sum(value) / len(values)
print(temp/ilosc)
