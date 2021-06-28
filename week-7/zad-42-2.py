
try:
    content = input('podaj teks do odwrócenia')
    if content == '':
        raise ValueError('Tekst nie został podany!')
    print(content[::-1])
except ValueError as e:
    print(e)

#zad 42-4

fruits = []
try:
    for _ in range(0, 10):
        fruit = input('podaj nazwę owoca: ')
        if fruit in fruits:
            raise ValueError('ten owoc już jest ! ')
        fruits.append(fruit)
except ValueError as e:
    print(e)

print(fruits)

# wer 2  łapie wyjątek ale ponieważ jest wewnątrz pętli pozwala pracować ddalej do końca pętli
# czyli zbierze całą baze
# łapanie wyjątków jest lepsze od QUIT ponieważ umożliwia nam wykonanie jakiejś czynności kończącej np:
# zamkniećie połączenia z bazą danych ! zapis danych itp

fruits = []

for _ in range(0, 10):
    try:
        fruit = input('podaj nazwę: ')
        if fruit in fruits:
            raise ValueError('ten owoc już jest! ')
        fruits.append(fruit)
    except ValueError as e:
        print(e)

print(fruits)



