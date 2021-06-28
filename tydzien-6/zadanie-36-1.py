from math import pi


class Circle:
    def __init__(self, promien: float):
        self.promien = promien

    def calculate_field(self):
        return pi * self.promien ** 2

    def calculate_circumference(self):
        return pi * 2 * self.promien

if __name__ == '__main__':
    radius = int(input('podaj promień koła: '))
    promien = Circle(radius)


    print(f'pole {promien.calculate_field():.2f}')
    print(f'obwód: {promien.calculate_circumference():.2f}')


def test_circle_field():
    # given
    r = 10
    c = Circle(r)

    # when
    field = c.calculate_field()

    # then
    assert field == pi * r * r

def test_circle_circumference():
    # given
    r = 10
    c = Circle(r)

    # when
    circ = c.calculate_circumference()

    # then
    assert circ == pi * r * 2

