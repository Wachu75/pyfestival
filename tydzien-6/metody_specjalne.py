'''

__init__
__str__ reprezentacja tekstowa
__add__ dodanie dwóch obiektów
__div__ dzielenie
__sub__ odejmowanie
__eq__ porównanie dwóch obiektów ==
__ge__ porównanie obiektów >=
__le__ porównanie obiektów <=
__gt__ wieksze
'''

class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    # definując metode specjalną nadpisujemy zachwoanie printa
me = Person("Ja", "Krzysztof")
print(me) # -> Ja Krzysztof

# next ex

class Box:
    def __init__(self, capacity: int):
        self.capacity = capacity
    def __add__(self, other):
        total = self.capacity + other.capacity
        return Box(total)

box1 = Box(10)
box2 = Box(20)
box3 = box1 + box2
print(box3.capacity) # zapis ten powoduje że odwołujemy się do self.capacity to jest box1 natomiast box to other.capacity

# jezeli byśmy zwrócili total mieli byśmy liczbę natomiast Box(total) będzie to nowy obiekt o pojemności dwóch boxów

# ex 3

class Box:
    def __init__(self, capacity: int):
        self.capacity = capacity

    def __str__(self):
        return f'{self.capacity}'

    def __lt__(self, other):  # nadpisujemy sortowanie
        return self.capacity < other.capacity

boxes = [
    Box(10),
    Box(20),
    Box(30)
]

for box in boxes:
    print(box)


for box in sorted(boxes):
    print(box)


class LengthUnit:
    def __init__(self, value: int):
        self.value = value

    def __str__(self):
        return f'{self.value}'

    def __add__(self, other):
        total = self.value + other.value
        return LengthUnit(total)

    def __sub__(self, other):
        minus = self.value - other.value
        return LengthUnit(minus)

    def __eq__(self, other):
        return self.value == other.value

    def to_centimeter(self):
        equal = self.value / 10
        return equal

    def to_meter(self):
        return self.value / 10 / 100


value1 = LengthUnit(2200)
value2 = LengthUnit(100)
print(value1.to_centimeter()) # zamiana działa ale tylko jako rerturn z metody to_centimetr
value2.to_centimeter()
#print(value1)
# value3 = value1.to_centimeter() + value2.to_centimeter() # a to nie działa
value3 = value1 + value2
print(value3.value)
value3 = value1 - value2
print(value3.value)
value4 = LengthUnit(100)
value5 = value2 == value4
print(value5)