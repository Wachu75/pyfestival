class A:
    def __init__(self, val1: int, val2: int):
        self.val1 = val1
        self.val2 = val2

    #def showA(self):
    #   return f"{self.val1}, {self.val2}"

class B:
    def __init__(self, val1: int, a: A):
        self.val1 = val1
        self.a = a

    def showB(self):
        #return f"{self.val1}, {self.a.showA()}"
        return f"{self.val1}, {self.a.val1}, {self.a.val2}" #też działa <- i teraz to zgłupiałem czemu to mi nie działało ???!!!!

newA = A(1,2) #tworzę obiekt instancją klasy A o nazwie newA z parametrami 1,2

newB = B(3,newA) # tworzę obiekt instancję klasy B o nazwie newB z parametrami 3 i obiektem newA klasy A

#print(newA.showA()) # mogę odwołąć się do metody w klasie A przy czym co jeśli nie chcę mieć do tego dostępu
# ponieważ dostęp ma mieć tylko klasa B, czy będzie to później omówione w następnych lrekcjach ? odp. chyba chodzi o enkapsulację
# czyli ukrywanie przed niepowołanym dostępem więc raczej się zagalopowałęm w myśleniu i coś pomyliłem :-(
print(newB.showB()) # mam dostęp do metody z clasy B która w sobie ma dostęp do metody a klasy A
# a co jeżeli chciałbym w showB mieć dostęp do self.a.val1 <- o dziwo nie wiem co było nie tak że to nie działało ?
print(newB.a.val1) # po dopisaniu tej linijki już kompletnie nic nie rozumiem !!! nie mogę znaleźć błedu w moim myśleniu
# co robiłem do tej pory niewłaściwie bo nie mogłem uzyskać -> obiektKlasyB.ObiektKlasyA.WłaściwośćPolaXzKlasyA
# drugi dzień nad tym siedzę :-( a teraz nagle nie wiedzić czemu napisałem no i uzyskałem to co chciałem i jest to zgodne z tym
# w jaki sposób sobie to wyobrażałem w głowie tzn. myślałem, że tak to ma działać ale nie działało ?

meeting1 = ('a', 1)
meeting2 = "spotkanie"
meetings = {}

meetings[0] = meeting1
meetings["2020-01-01"] = meeting1
meetings[23] = meeting2

print(meetings)
