
names = [
    'a','b','c','d','e','f','g'
]

for id, name in enumerate(names):
    print(f'{id}. {name}')
try:
    number = int(input('ktorą litere wybierasz'))
    print(names[number])

except IndexError:
    print('nie ma takiego imienia')
except (TypeError, ValueError) as error:
    print('ERROR: ', error)


