'''
ukrywanie pól danej klasy dla innych klas. chronimy w ten sposób przd nieprzewidzianym wywołaniem metod

'''

class Bank:
    def __init__(self):
        self._money = 1000 *1000

    def withdraw(self, amount: int):
        if amount > self._money:
            return 0

        self._money -= amount

        return amount

    def deposit(self, amount: int):
        self._money += amount

    def _convert_to_sth(self): # _ podkreslenie również informowanie o tym że to metoda ukryta
        pass

