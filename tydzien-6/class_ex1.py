class wektor3d:
    '''Klasa do działań na trójwymiarowych wektorach'''
    # Jeżeli zdefiniujemy w klasie metody __getitem__(self,key) oraz __setitem__(self,key,value), to możemy
    # obiekty (instancje) traktować jak słownik. Rozbudowana klasa wektor3d:
    # Uzyskujemy w ten sposób nie tylko łatwy dostęp do współrzędnych wektora, ale i potencjalnie niebezpieczną
    # możliwość zmiany struktury istniejącego obiektu.
    # Możliwość zmiany struktury istniejącego obiektu istnieje zawsze (tzn. nie zależy od tego czy zdefiniowane
    # są metody __setitem__ i __getitem__) i zawsze jest niebezpieczna.
    #
    def __getitem__(self, key):
        return self.wektor[key]
    def __setitem__(self, key, value):
        while len(self.wektor) <= key:
            self.wektor.append(0)
        self.wektor[key] = value
    # Warto również zdefiniować w klasie metodę __str__. Jest ona odpowiednikiem metody toString znanej z Javy i C#.
    # Jeżeli metoda ta jest zdefiniowana w klasie K, a zmienna ob jest typu K, to polecenie print ob jest równoważne
    # poleceniu print ob.__str__(). Jeszcze raz rozbudujemy klasę wektor3d:
    def __str__(self):
        s = ""
        for k in self.wsp.keys():
            s += k + " = " + str(self.wektor[self.wsp.get(k)]) + "\n" #tworzymy stringa s gdzie k są kolejnymi kluczami
            # wsp dla nas są to x y z
        return s
    def __init__(self):
        self.wektor=[0,0,0]
        self.wsp = {"x":0,"y":1,"z":2}

    def setVector(self,wektor):
        self.wektor = wektor
    def setCoordinateByNumber(self,which,coordinate):
        self.wektor[which] = coordinate
    def setCoordinateByName(self,which,coordinate):
        self.setCoordinateByNumber(self.wsp[which],coordinate)
    def move(self,wektor):
        for i in range(3):
            self.wektor[i] = self.wektor[i]+wektor[i]
    def add(self,wektor):
        for i in range(3):
            wektor[i] = wektor[i]+self.wektor[i]
        wynik = wektor3d()
        wynik.setVector(wektor)
        return wynik
    def show(self):
        print(self.wektor)

w = wektor3d()
w.show()

w.setVector([1,2,3])
w[2] = 9  # dzieki __getitem__ uzyskujemy łatwy dostęp do współrzędnhych wektora
 # w[5] = 1 ale również niebezpieczeństwo zmiany struktury IndexError:

#w.name = "wektor w" # dodanie pola do istniejącego obiektu
#del w.wektor # usunięcie pola z istniejącego obiektu
w.__str__()
print(w)
w.show()


w.move([2,4,6])
w.show()

w.setCoordinateByName("x", 5)
w.show()

z = w.add([1,0,0])
z.show()
w.show()

