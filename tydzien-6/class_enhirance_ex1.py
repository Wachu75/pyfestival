'''
Dziedziczenie
Jeżeli chcemy zdefiniować klasę pochodną P dziedziczącą po klasie bazowej B, to początek definicji klasy wygląda tak: class P(B):. W klasie pochodnej możemy zmieniać istniejące atrybuty (właściwości), możemy też dodawać nowe atrybuty.
Klasa bazowa Ssak. Do przechowywania informacji o obiekcie typu Ssak wykorzystywany jest słownik (typ dict).
Klasa pochodna Wilk nie dodaje nowych atrybutów, zmienia konstruktor, nie zmienia metody whoAreYou, nadpisuje metodę demo.
'''

class Ssak:
    def __init__(self,imie="???"):
        self.dane = {"kind":"Ssak","name":imie,"legs":"???","voice":"???"}
    def whoAreYou(self):
        print(self.dane["kind"])
        print("Name: "+self.dane["name"])
        print("Legs: "+str(self.dane["legs"]))
        print("Voice: "+self.dane["voice"])
    def demo(self):
        return "mammal"

class Wilk(Ssak):
    def __init__(self,imie="Kazan"):
        self.dane = {"kind":"Wilk","name":imie,"legs":4,"voice":"uuuuuuuuuuu"}
    def demo(self):
        return "wolf"
# Klasa pochodna Czlowiek zmienia konstruktor, dodaje dwie nowe metody, zwiększa ilość przechowywanych informacji (nazwisko), nadpisuje metodę demo.

class Czlowiek(Ssak):
    def __init__(self,imie="???"):
        self.dane = {"kind":"Czlowiek","name":imie,"legs":2,"voice":"Witaj"}
        self.dane["nazwisko"]="???"
    def setNazwisko(self,nazwisko):
        self.dane["nazwisko"]=nazwisko
    def getNazwisko(self):
        return self.dane["nazwisko"]
    def demo(self):
        return "man"

# Przykład wykorzystania (przy niezbyt realistycznym założenie, że klasy zostały zdefiniowane interaktywnie, nie jest zatem potrzebne polecenie import):

w = Wilk("barii")
w.whoAreYou()
man = Czlowiek()
print(man.getNazwisko())
print(man.setNazwisko("Kowalski"))
print(man.getNazwisko())

# Klasa Kobieta dziedziczy po klasie Czlowiek (dziedziczenie "wielopokoleniowe"), w takim przypadku bywa potrzebne jawne wywołanie metody __init__.

class Kobieta(Czlowiek):
    def __init__(self,imie="Maria"):
        Czlowiek.__init__(self,imie)
        self.dane["kind"] = "Kobieta"

# Python pozwala na wielokrotne dziedziczenie, jeżeli klasa P dziedziczy po klasach B1,...,Bn: class P(B1,...,Bn):, to atrybuty szukane są od lewej (klasa B1) do prawej (klas Bn).

class Wilkolak(Wilk,Czlowiek):
    def demo(self):
        return "werewolf"

Wilkolak().whoAreYou()

class Wilkolak(Czlowiek,Wilk):
    def demo(self):
        return "werewolf"

Wilkolak().whoAreYou()

# W klasie bazowej Ssak została zdefiniowana metoda demo. Została ona nadpisana w klasach pochodnych Wilk, Czlowiek i Wilkolak. Można na rzecz obiektu z klasy pochodnej wywołać (nadpisaną w tej klasie) metodę z klasy bazowej.

w = Wilkolak()
w.demo()
Wilk.demo(w)
Ssak.demo(w)

# Atrybuty klasy i składowe (elementy) prywatne
# Niekiedy potrzebne są takie atrybuty instancji (zmiennych obiektowych), które mają identyczną wartość dla wszystkich instancji. Typowy przykład, to informacja o ilości istniejących instancji. W wielu językach takie atrybuty nazywane są statycznymi (słowo kluczowe static) lub zmiennymi klasy. W poniższym przykładzie zmienna klasy licznik, przechowuje informację ile razy wywołany był konstruktor klasy L.
# Definicja atrybutów klasy znajduje się poza konstruktorem.

class L:
    licznik = 0
    def __init__(self):
        self.__class__.licznik+=1
L.licznik
a = L()
L.licznik
a.licznik
for i in range(50):
    L()
a.licznik

# Python dopuszcza by w klasie istniały zmienne klasowe i zmienne obiektowe o takiej samej nazwie. Rozróżnienie zmiennej klasowej i zmiennej obiektowej uzyskujemy korzystając ze słowa kluczowego __class__

class L:
    licznik = 0 #zmienna klasowa licznik, konstruktor nie zmienia jej wartości
    def __init__(self):
        self.licznik+=1 #zwiększana jest wartość zmiennej obiektowej licznik
a=L()
a.licznik
a.__class__.licznik
L.licznik

# Elementy prywatne
# Dostęp do elementów prywatnych jest ograniczony. W Pythonie nie ma słowa kluczowego private, element jest prywatny jeżeli jego nazwa zaczyna się od __ (podwójne podkreślenie) i nie kończy się podwójnym podkreśleniem. Zgodnie z dokumentacją jest to tylko umowa, która może ulec zmianie.
# Co może byc prywatne:
#
#     atrybut (pole) w klasie - może być używany tylko przez metody tej klasy,
#     metoda w klasie - może być wywołana tylko z wnętrza klasy.
#
# Plik prywatne.py zawiera definicję klasy z polem prywatnym i metodą prywatną. lecz go nie mam :-(

class Test:
    def __init__(self):
        self.__prywatne = 2
        self.publiczne = 5
    def pokaz(self):
        self.__pokaz()
    def __pokaz(self):
        print("publiczne "+str(self.publiczne))
        print("prywatne "+str(self.__prywatne))
#import prywatne
#t = prywatne.Test()
#t.__prywatne

#AttributeError: Test instance has no attribute '__prywatne'
#t.publiczne #=> 5
#t.__pokaz() #=>
...
#AttributeError: Test instance has no attribute '__pokaz'
#t.pokaz() #=>
#publiczne #5
#prywatne #2