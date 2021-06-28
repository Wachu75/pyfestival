
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

print(t)
print(source)
