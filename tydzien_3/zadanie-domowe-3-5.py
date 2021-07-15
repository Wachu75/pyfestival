# Przygotuj funkcje, która za pomocą wyrażenia list comprehension będzie potrafiła przefiltrować liczby parzyste z listy
# przekazanej w argumencie.

listValues = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

def filterOfEvenValues(data):
    return [n for n in data if n % 2 == 0]

print(filterOfEvenValues(listValues))

