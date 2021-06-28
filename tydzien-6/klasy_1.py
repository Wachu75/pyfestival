
class Student:
    def __init__(self, firs: str, last: str,sem: int = 1):
        self.firs = firs
        self.last = last
        self.sem = sem

    def promotion(self):
        self.sem += 1

    def hello(self):
        return f'jestem {self.firs} {self.last}, semestr {self.sem}'

g = Student('a', 'b', 1)
# Judi = g  !!! spowoduje utworzenie przezwiska referencji mamy 2 zmienne wskazujące na to same miejsce pamieci
# jest to pomocne gdy chcemy przekazać jakiś obiekt do jakiejś metody nie musimy z tej metody zwracać tego obiektu
# w całości , wystarczy że w tej metodzie zmodyfikujemy ten obiekt i na zewnątrz też będzie on zmodyfikowany
# należy spojrzeć na to z perspektywy tego co do tej pory mam przeszkadzało jeżeli odbieraliśmy jakąs liczbę to musieliśmy
# ją jeszcze zwrócić i urzywać GLOBAL

Judi = Student('Judi', 'Jetson', 2)

print(g) #jest to inf jakiej clasy jest g <__main__.Student object at 0x0000021FA860F970>
print(g.firs, g.last)
print('semestr: ', g.sem)
print(g.hello())
g.promotion()
print('semestr: ', g.sem)
print(g.hello())
x = g # UWAGA NIE TWORZYMY NOWEGO OBIEKTU JEST TO REFERENCJA PRZEZWISKO KOPIA
print(Judi.firs, " ", Judi.last)

