
from datetime import date


class Product:
    def __init__(self, price: float):
        self.price = price

    def calculate_netto(self, vat: float):
        self.vat = vat
        # 23 + 100 = 123 / 100 = 1.23
        vat = (self.vat + 100) / 100
        netto = self.price / vat

        return round(netto, 4)

    def get_brutto(self):

        return self.price


class Booking:
    def __init__(self, start_date: date, end_date: date):
        self.end_date = end_date
        self.start_date = start_date

    def start(self):
        return self.start_date

    def end(self):
        return self.end_date

    def get_difference(self):
        difference = self.end_date - self.start_date
        #print(difference.days)
        return difference.days


class Reservation(Product, Booking):
    def __init__(self, price: float, start_date: date, end_date: date):
        Product.__init__(self, price)
        Booking.__init__(self, start_date, end_date)
        # Product.__init__(self.price)                       # tu miałem błąd
        # Booking.__init__(self.start_date, self.end_date)   # tu miałem błąd


    def pay_for_one_day(self):

        return Product.get_brutto()

    def start(self):

        return Booking.start()

    def end(self):

        return Booking.end()

    def spend_date(self):

        return Booking.get_difference()

    def total_cost(self):
        total = self.get_difference() * self.get_brutto() # tu miałem błąd Product.get_difference() - ...

        return total


standard_room = Product(120)
print(standard_room.price)
print(standard_room.calculate_netto(23))
start = date(2021,7,1)
endDate = date(2021,7,3)
pobyt1 = Booking(start, endDate)
print(pobyt1.start())
print(pobyt1.end())
print(pobyt1.get_difference())
rezerwacja1 = Reservation(100, start, endDate) # tu miałem błąd w inny sposób próbowałem utworzyć instancję
# rezerwacja1 = Reservation(standard_room, pobyt1) jako dwie instancje innych klas
print(rezerwacja1.total_cost())