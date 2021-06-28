leter = []
temporary = [*range(65, 91, 1)]
for i in temporary:
    leter.append(chr(i))
temporary = [*range(97,123,1)]
for i in temporary:
    leter.append(chr(i))
#print(leter)

for number, leter in enumerate(leter, start=1):
    print(number, leter, end=', ')


