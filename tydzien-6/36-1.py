from math import pi

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def licz_pole(self):
        return pi * self.radius ** 2

    def licz_obwod(self):
        return 2 * pi * self.radius

if __name__ == '__main__':
    r = float(input('podaj promien: '))
    c = Circle(r)
    print(f'pole = {c.licz_pole()}')
    print(f'obwód = {c.licz_obwod()}')


def test_circle_field():
    # given
    r = 10
    c = Circle(r)

    # when
    field = c.licz_pole()


    # then
    assert field == pi * r ** 2


def test_circle_area():
    r = 10
    c = Circle(r)

    area = c.licz_obwod()

    assert area == 2 * pi * r




