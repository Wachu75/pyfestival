
class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_b = side_b
        self.side_a = side_a

    def aera_rectangle(self):
        return self.side_a * self.side_b

    def perimeter_rectangle(self):
        return self.side_a * 2 + self.side_b * 2

def test_area_rectangle():
    rect1 = Rectangle(side_a=10, side_b=20)

    aera = rect1.aera_rectangle()

    assert aera == 200


