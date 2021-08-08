
class Car:
    def __init__(self, name, price, max_speed):
        self.name = name
        self.price = price
        self.max_speed = max_speed

    def get_info(self):
        return f'{self.name}, cena: {self.price}, predkosc: {self.max_speed}'

class Collection:
    def __init__(self): # nie przekazuje żadnych agrumentów
        self.items = [] #potrzebuje tylko stworzyć pustą listę

    def add_item(self, item):       # dodanie do naszej listy elementu
        self.items.append(item)

    def get_items(self, key, reverse=False):
        return sorted(self.items, key=key, reverse=reverse)


if __name__ == '__main__':
    collection = Collection()

    for _ in range(2):
        name = input('nazwa ')
        price = input('cena ')
        max_speed = input('predkosc ')
        collection.add_item(Car(name, price, max_speed))

    for car in collection.get_items(key=lambda c: c.price, reverse=True):  # key wymaga lambda która zwróci wartość po której ma być sortowanie
        print(car.get_info())       #lambda c: c.price pobiera właściwość obiektu c należacego classy Car właściwość ta to price

def test_class_car():
    car = Car(name='Polonez', price=1000, max_speed=120)

    assert isinstance(car, Car)

    assert car.name == 'Polonez'

    assert car.price == 1000

    assert car.max_speed == 120