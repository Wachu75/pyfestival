for i in reversed(range(1, 5)):
    print('*' * i)

names = 'ala', 'olga', 'janek', 'krzysztof', 'genowefa', 'aleksandra'
max = ''
for name in names:
    #print(name)
    if len(name) > len(max):  max = name
    #print(max)

print(max)


