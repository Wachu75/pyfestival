# Przygotuj funkcję, która zliczy ilość znaków w tekście zawierających się wewnątrz
# nawiasów okrągłych. Nawiasy mogą występować w tekście wielokrotnie, nigdy nie
# będą się w sobie zawierać.

test = "tego nie ma liczyć(to ma policzyc)(to też)"



def searchBracket(inputStr):
    indexStart = 0
    indexEnd = 0
    temp = ""
    output = ""
    for index, s in enumerate(inputStr):
        if s == "(": indexStart = index

        if s == ")": indexEnd = index

        temp = (test[indexStart+1:indexEnd])

        output = output + temp

    return len(output)

print(searchBracket(test))

