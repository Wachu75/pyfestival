'''
Kolejność podawania clas z których dziedziczymy ma znaczenie !!!

class Pojazdy:
    pass


class Jezdace(Pojazdy):
    pass


class Plywajace(Pojazdy):
    pass


class Amfibia(Jezdace, Plywajace):
    pass

'''


class AddCalc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b


class SubCalc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sub(self):
        return self.a - self.b


class Calculation(AddCalc, SubCalc):
    def __init__(self, a, b):
        AddCalc.__init__(self, a, b)
        SubCalc.__init__(self, a, b)

    def run(self):
        return self.add() + self.sub()

# ************************************************************************

class A:
    def run(self):
        print('Method in class A')

class B:
    def run(self):
        print('Method in class B')

    def run1(self):
        print('Method run1 from class B')

class Child(A, B):  # Jeżeli znalazł def run w clasie 1 czyli A to tą metodę wykona ! Kolejność ma znaczenie !!!
    # chyba że w B jest coś nowego
    def go(self):
        self.run()
        self.run1()

a = Child()
a.go()

