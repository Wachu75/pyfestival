class Product:
    def __init__(self, name: str, price: float):
        self._price = price
        self._name = name

    def get_price(self) -> float:
        return self._price


class ListItem:
    def __init__(self, product: Product, quantity: float):
        self._quantity = quantity
        self._product = product

    def get_quantity(self) -> float:
        return self._quantity

    def add_quantity(self, quantity):
        self._quantity += quantity

    def decrease_quantity(self, quantity):
        self._quantity -= quantity

    def get_sub_total(self):
       return self._quantity * self._product.get_price()

    def get_product(self):
        return self._product


class List:
    def __init__(self):
        self._items = []

    def add_item(self, product: Product, quantity: float):
        for item in self._items:
            if item.get_product() == product:
                item.add_quantity(quantity)
                return

        self._items.append(
            ListItem(product, quantity)
        )

    def remove_item(self, product: Product, quantity: float):
        for item in self._items:
            if item.get_product() == product:
                item.decrease_quantity(quantity)
                return


    def list_item(self):
        return self._items

    def calculate_total_cost(self) -> float:
        total = 0
        for item in self._items:
            total += item.get_sub_total()

        return total



product = Product('mleko', 3.23)
product1 = Product('mleko', 3.23)
to_buy = List()

to_buy.add_item(product, 3)


to_buy.add_item(product, 3)




