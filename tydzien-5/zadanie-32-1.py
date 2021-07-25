
source = []
t =[]
with open('transakcje-1.csv', encoding='utf8') as file_open:
    for data in file_open:
        result = data.split(',')
        #print(type(data))
        #print(result[-1])
        # for indata in result:
        #     result = indata.split()
        #     print(result)

        # if result[-1] == '\n':
        #     pass
        #t = map(lambda result: result.strip(), t)
        t.append(result[-1].strip())
        source.append(result)
t = [s for s in t if s.isnumeric()]

with open('przychody.txt', 'w') as file:
    for x in t:
        file.write(f'{x}\n')


print(t)
print(source)
value = 0
with open('przychody.txt') as file:
    for line in file:
        value += int(line)

print(value)