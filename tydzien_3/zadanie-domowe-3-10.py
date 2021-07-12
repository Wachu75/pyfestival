# Przygotuj funkcję, która odbierze od użytkownika procent zdobytych punktów, a w
# odpowiedzi zwróci ocenę jaką otrzymał użytkownik.
# Minimum procentowe Ocena
# <45% niedostateczny
# 45% dopuszczający
# 55% dostateczny
# 80% dobry
# 90% bardzo dobry
# 95% celujący

#może dwie listy z zakresem procentowym i oceną
def percentValue(percent):
    mark = {0: 'niedostateczny',45: 'dopuszczający',55: 'dostateczny',80: 'dobry',90: 'bardzo dobry',95: 'celujący'}
    keyList = sorted(mark.keys())

    for key, value in enumerate(keyList):
        print(key)
        print(value)
        if value >= percent: print(keyList[key+1])
        #print(type(percent))

    return None

print(percentValue(45))

# keyList=sorted(d.keys())
# for i,v in enumerate(keyList):
#     if v=='eeee':
#         print d[keyList[i+1]]
#         print d[keyList[i-1]]