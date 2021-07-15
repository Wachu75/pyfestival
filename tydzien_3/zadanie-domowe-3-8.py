#Przygotuj funkcję, która odbierze argument, który określa
#ile kolejnych wyrazów ciągu Fibonacciego ta funkcja zwróci.
#Ciąg fibonacciego to taki ciąg, gdzie każdy kolejny wyraz
#jest sumą dwóch poprzednich.

def fibonacci(end):
    values = [1,1,]
    index = 1
    while len(values) <= end-1:
        temp = values[index] + values[index-1]
        values.append(temp)
        index += 1
    return values

print(fibonacci(10))

