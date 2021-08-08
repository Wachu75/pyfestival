'''
skaraca zapis tzn nie urzywamy nawiasów na koncu
tworzymy metody statyczne
metody dostępowe
'''

class Product:
    def __init__(self, price):
        self.price = price
        self._discount = 0.1

    def __str__(self):
        return f'{self.price}'

    @property
    def new_price(self):
        return self.price

    @new_price.setter
    def new_price(self, new_price):
        self.price = new_price

    @property
    def discount(self):
        return self._discount

    @property
    def discounted_price(self):
        self.price = self.price - (self.price * self._discount)
        return self.price

    @discount.setter
    def discount(self, new_discount):
        if 0 <= new_discount <= 1:
            self._discount = new_discount

    @discount.deleter
    def discount(self):
        self._discount = 0

car = Product(1000)
print(car)
print(car.discounted_price)
del car.discount
print(car.discounted_price)
print(car.discount)
car.discounted_price
print(car)
print(car.discount)
print(car.discounted_price)
car.price = 1000
print(car.discount)
car.discounted_price
print(car.new_price)
print(car)
