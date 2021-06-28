
class Apple:
    def __init__(self, color, taste, kind):
        self.color = color
        self.taste = taste
        self.kind = kind


class Basket:
    def __init__(self):
        self.apples = []

    def add(self, apple: Apple):
        self.apples.append(apple)


class Report:
    def __init__(self, basket):
        self.basket = basket

    def get_for_color(self):
        report = {}
        for apple in self.basket.apples:
            if apple.color not in report:
                report[apple.color] = 0

            report[apple.color] +=1

        return report


def test_apple_collection():
    #given
    apple1 = Apple('czerwone', 'slodkie', 'dojrzałe')
    apple2 = Apple('czerwone', 'slodkie', 'dojrzałe')
    apple3 = Apple('zielone', 'slodkie', 'dojrzałe')
    basket = Basket()

    #wehen
    basket.add(apple1)
    basket.add(apple2)
    basket.add(apple3)

    report = Report(basket)
    color = report.get_for_color()

    #then
    assert color == {
        'czerwone': 2,
        'zielone': 1
    }