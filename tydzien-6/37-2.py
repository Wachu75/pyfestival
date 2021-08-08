
class Apple:
    def __init__(self, color, taste, kind):
        self.color = color
        self.taste = taste
        self.kind = kind


class Basket:
    def __init__(self):
        self.apples = []        # tworzymy pustą listę

    def add(self, apple: Apple):    # w metodzie odbieramy obiekt klaesy Apple
        self.apples.append(apple)   # dodajemy kolejne przekazane obiekty do listy

# nie działa !!!

    # def showBasket(self):
    #     report = {}
    #     for basket.apples in self.apples:
    #         if basket.apples not in report:
    #             report[basket.apples]  = 0
    #         report[basket.apples] +=1
    #     #temp = self.apples[0]
    #     return report

class Report:
    def __init__(self, basket):     # basket zaiwera apple czyli aby dostać się do apples mamy basket.apples.
        self.basket = basket
        #print(self.basket.apples[])
    def get_for_color(self):        # metoda która zlicza
        report = {}                 # pusty słownik
        for aples in self.basket.apples: # iterujemy po koszyku który zawiera jabłka apples1 apples2 apples3 itd... apples zawiera ('xxx','zzz','aaa')
            #print(self.basket.apples)
            print(aples.color)
            if aples.color not in report:   # chcąc iterować po xxx musimy to określić dla nas jest to apples.color gdzie color to
                                            # atrybut obiektu klay Apple
                report[aples.color] = 0     # jeżeli tego klucza nie ma jeszcze w raport to utwórz taki klucz i nadaj mu wartość początkową 0

            report[aples.color] +=1         # ponieważ po wyjsciu z if dodajemy wartość nie potrzebujemy else taki trik :-)

        return report

apple1 = Apple('czerwone', 'slodkie', 'dojrzałe')
apple2 = Apple('czerwone', 'slodkie', 'dojrzewajace')
apple3 = Apple('zielone', 'slodkie', 'dojrzewajace')
apple4 = Apple('zielone', 'slodkie2', 'dojrdzewajace')
apple5 = Apple('zielone', 'slodk2ie', 'dojrzewajgace')
basket = Basket()
basket.add(apple1)
basket.add(apple2)
basket.add(apple3)
basket.add(apple4)
basket.add(apple5)
report = Report(basket)
color = report.get_for_color()
print(color)
#print(Basket.showBasket())  # nie działa
# def test_apple_collection():
#     #given
#     apple1 = Apple('czerwone', 'slodkie', 'dojrzałe')
#     apple2 = Apple('czerwone', 'slodkie', 'dojrzałe')
#     apple3 = Apple('zielone', 'slodkie', 'dojrzałe')
#     basket = Basket()
#
#     #wehen
#     basket.add(apple1)
#     basket.add(apple2)
#     basket.add(apple3)
#
#     report = Report(basket)
#     color = report.get_for_color()
#
#     #then
#     assert color == {
#         'czerwone': 2,
#         'zielone': 1
#     }