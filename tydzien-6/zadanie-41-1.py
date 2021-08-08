from datetime import datetime

class Saving:
    def __init__(self, data: datetime, quality: float):
        self._quality = quality
        self._data = data

    def __str__(self):
        return f'{self._data}, {self._quality}'

    @property
    def created_at(self):
        return self._data

    @property
    def amount(self):
        return self._quality

    @amount.setter
    def amount(self, amount):
        if amount > 0:
            self._quality = amount

    def __repr__(self):
        return f'{self._data.strftime("%d.%m.%Y")}-{self._quality}'

class Savings:
    def __init__(self):
        self._savings = []

    def raport(self):
        for prod in self._savings:
            print(f'id: {self._savings.index(prod)}')
                      #f'  produkt: {prod.get_list_products_name()}')

    def add_saving(self, saving: Saving):

        self._savings.append(saving)
        #print(self._savings)


    @property
    def total(self):
        return sum([saving.amount for saving in self._savings])
        #        return sum([saving._quality for saving in self._savings])


zakupy1 = Saving(datetime(2012, 2, 2),456)
zakupy2 = Saving(datetime(2021, 1, 30), 600)
kasa = Savings()
kasa.add_saving(zakupy1)
kasa.add_saving(zakupy2)
raport_stanu = kasa.raport()
print(raport_stanu)
print(kasa.total)

for saving in kasa._savings:
    print(saving)