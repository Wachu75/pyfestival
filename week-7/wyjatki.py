'''
jak wysłać wyjątek?
    raise Exception('text')
wer 2  zad-42-2.py
 łapie wyjątek ale ponieważ jest wewnątrz pętli pozwala pracować ddalej do końca pętli
 czyli zbierze całą baze
 łapanie wyjątków jest lepsze od QUIT ponieważ umożliwia nam wykonanie jakiejś czynności kończącej np:
 zamkniećie połączenia z bazą danych ! zapis danych itp

Możemy twożyć własne wyjątki:
class ValueToSmall(Exception):
    pass : tu oczywiście właściwy kod

'''
try:
    while True:
        value = int(input('Podaj liczbę: '))
        if not value % 5 == 0:
            raise Exception('nie podzielna przez 5 ')

        print(value)
except Exception as e:
    print(e)

