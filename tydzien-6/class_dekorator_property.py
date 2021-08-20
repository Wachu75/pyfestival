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

'''
nextexample

'''

class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        print("getter of x called")
        return self._x

    @x.setter
    def x(self, value):
        print("setter of x called")
        self._x = value

    @x.deleter
    def x(self):
        print("deleter of x called")
        del self._x


c = C()
c.x = 'foo'  # setter called
foo = c.x    # getter called
del c.x      # deleter called
