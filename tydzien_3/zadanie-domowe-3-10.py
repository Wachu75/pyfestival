# Przygotuj funkcję, która odbierze od użytkownika procent zdobytych punktów, a w
# odpowiedzi zwróci ocenę jaką otrzymał użytkownik.
# Minimum procentowe Ocena
# <45% niedostateczny
# 45% dopuszczający
# 55% dostateczny
# 80% dobry
# 90% bardzo dobry
# 95% celujący


def percentValue(percent):
    mark = [(0,'niedostateczny'),(45, 'dopuszczający'),(55, 'dostateczny'),(80, 'dobry'),(90, 'bardzo dobry'),(95, 'celujący'),(101, 'celujacy')]
    keyList = enumerate(mark)

    for a, b in keyList:
        if a == (len(mark)-1): break
        if int(mark[a][0]) <= percent and int(mark[a+1][0]) > percent: return mark[a][1]

    return None

#print(percentValue(55))

percent = int(input('podaj uzyskany w procentach wynik egzaminu: '))
print(percentValue(percent))
