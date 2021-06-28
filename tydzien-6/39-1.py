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

    def get_quantity(self):
        return self._quantity

    def get_sub_total(self):
        return self._quantity * self._product.get_price()

    def get_product(self) -> Product:
        return self._product

    def add_quantity(self, quantity):
        self._quantity += quantity

    def decrease_quantity(self, quantity):
        self._quantity -= quantity


class List:
    def __init__(self):
        self._item = []

    def add_item(self, product: Product, quantity: float):
        for item in self._item:
            if item.get_product() == product:
                item.add_quantity(quantity)
                return

        self._item.append(
            ListItem(product, quantity)
        )

    def remove_item(self, product: Product, quantity: float):
        for item in self._item:
            if item.get_product() == product:
                item.decrease_quantity(quantity)
                return

    def list_item(self):
        return self._item

    def calculate_total_price(self) -> float:
        total = 0
        for item in self._item:
            total += item.get_sub_total()

        return total


def test_add_item_to_list_once():
    # given
    product = Product('chleb', 4.30)
    to_buy = List()

    # when
    to_buy.add_item(product, 3)

    # then
    assert to_buy.calculate_total_price() == 4.3 * 3
    assert len(to_buy.list_item()) == 1


def test_add_the_same_item_to_list_twice():
    # given
    product = Product('chleb', 4.30)
    to_buy = List()

    # when
    to_buy.add_item(product, 3)
    to_buy.add_item(product, 3)

    # then
    assert to_buy.calculate_total_price() == 4.3 * 6
    assert len(to_buy.list_item()) == 1


def test_add_two_diferent_products_to_list():
    # given
    product1 = Product('chleb', 4.30)
    product2 = Product('maslo', 6.0)
    to_buy = List()

    # when
    to_buy.add_item(product1, 1)
    to_buy.add_item(product2, 1)

    # then
    assert len(to_buy.list_item()) == 2
    assert to_buy.calculate_total_price() == 10.30
