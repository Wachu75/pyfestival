'''
https://www.samouczekprogramisty.pl/wzorzec-projektowy-metoda-wytworcza/

'''


class PostOffice:
    def deliver(self, parcel):
        print(f"Parcel {parcel} was delivered by PostOffice")


class Courier:
    def deliver(self, parcel):
        print(f"Parcel {parcel} was delivered by Courier")


class Pigeon:
    def deliver(self, parcel):
        print(f"Parcel {parcel} was delivered by Pigeon")


class OrderLifecycle:
    def process_order(self, order_id):          # cd z lini 53: odbieram argument "order_2" i następnie do zm parcel przypisuję self. prepare_parcel
        parcel = self.prepare_parcel(order_id)  #
        delivery_service = self.delivery_service()# tutaj do zmiennej del... przypisuję tak naprawdę wynik zwrócony przez metodę z
# klasy class CourierOrderLifecycle(OrderLifecycle): czyli wywołanie clasy Courier: i dopiero teraz mogę wywołać metodę deliver
        delivery_service.deliver(parcel) #

    def prepare_parcel(self, order_id):
        parcel = f"[sampro:{order_id}]"
        print(f"Parcel {parcel} was prepared")
        return parcel

    def delivery_service(self):
        return PostOffice()


class PigeonOrderLifecycle(OrderLifecycle):
    def delivery_service(self):
        return Pigeon()


class CourierOrderLifecycle(OrderLifecycle):
    def delivery_service(self):
        return Courier()


if __name__ == "__main__":
    courier_order = CourierOrderLifecycle() # tworzę instancję klasy CourierOrderLifecycle dziedziczącą po OrderLifeCycle
# tym samym w lini następnej wywołując na instancji obiektu courier_order. metode process_order(...) której nie ma w class CourierOrderLifeCycle
# wywołuję już metodę z klasy po której dziedziczy CourierOrderLifeCycle czyli z OrderLifecycle metodę process_order(..)
    courier_order.process_order("order_2")
# skok do lini 22

    pigeon_order = PigeonOrderLifecycle()
    pigeon_order.process_order("order_3")

    post_office_order = OrderLifecycle()
    post_office_order.process_order("order_1")


