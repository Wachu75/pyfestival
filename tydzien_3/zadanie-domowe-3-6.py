#Przygotuj funkcję, która za pomocą list comprehension przefiltruje tylko słowa, których długość jest większa od 4
#i mniejsza od 8.


def scopeFromMinToMax(data, startPosition = 4, endPosition = 8):

    a = [data[word] for word in range(len(data)) if len(data[word])>startPosition and len(data[word])<endPosition]# if len(data)>startPosition and len(data)<endPosition]

    return a

print(scopeFromMinToMax(['alk', 'asdwewdfergghy', 'as', 'vfgrty'], 2, 8))

