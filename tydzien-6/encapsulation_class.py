'''
ukrywanie pól danej klasy dla innych klas. chronimy w ten sposób przd nieprzewidzianym wywołaniem metod
do definiowania używamy jednego podkreślenia _dana tak samo metody def _metoda(self):
enkapsulacja nie jest zabezpieczeniem przed innymi jest to tak jakby informacja uważaj nie uruchamiaj/zmieniaj z zewnątrz

'''

class Bank:
    def __init__(self):
        self._money = 1000 * 1000

    def withdraw(self, amount: int): # enkapsulacja przydaje się gdy chcemy dokonać np porównania czegoś z zewnątrz z wartością ukrytą
        if amount > self._money:
            return 0

        self._money -= amount

        return amount

    def deposit(self, amount: int):
        self._money += amount

    def _convert_to_sth(self): # _ podkreslenie również informowanie o tym że to metoda ukryta
        pass
    # metody prywatne wywołujemy tylko wewnątrz klasy bank


