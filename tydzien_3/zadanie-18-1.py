listatuplowa = [
    (1,2,3,4,5),
    (3,),
    (11,12,13,14,15,16)
]
for i in listatuplowa:
    #if (len(i) % 2 == 0):
    #if len(i) < 2:
        suma = sum(i)
        #print('parzyste')
        #print(suma)



parzysta = [sum(i) for i in listatuplowa if ((len(i) % 2 == 0) and (len(i) > 2))]

nieparzyste = [int(sum(i)/len(i)) for i in listatuplowa if ((len(i) % 2 == 1) and len(i) > 2)]

print(parzysta)
print(nieparzyste)
