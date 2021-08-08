
class Product:
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

class ListItem:
    def __init__(self, product: Product, quantity: float):
        self._product = product
        self._quantity = quantity

    def get_product_name(self):
        return self._product.get_name()

    def get_product_price(self):
        return self._product.get_price()

    def get_product_quantity(self):
        return self._quantity
        # return f'{self._quantity}'

    def modify_quantity(self, to_add):
        self._quantity = to_add

    def modify_price(self, new_price):
        self._product._price = new_price

    def get_data(self):
        return f'Nazwa: {self._product.get_name()}, Cena: {self._product.get_price()}, Ilość: {self._quantity}'


class List:
    def __init__(self, items):
        self._items = items

    def add_item(self, product: Product, quantity: float):
        for item in self._items:
            if item.get_product_name() == product.get_name():
                if item.get_product_price() != product.get_price():
                    modify_price = input(
                        f'Zmodyfikować cenę produktu z {item.get_product_price()} na {product.get_price()}? [t/n]: ')
                    if modify_price == 't':
                        item.modify_price(product.get_price())
                current = item.get_product_quantity()
                current += quantity
                return item.modify_quantity(current)

        self._items.append(ListItem(product, quantity))

    def remove_item(self, product: Product, quantity: float):
        for item in self._items:
            if item.get_product_name() == product:
                current = item.get_product_quantity()
                current -= quantity
                if current <= 0:
                    self._items.remove(item)
                else:
                    return item.modify_quantity(current)

    def list_items(self):
        for item in self._items:
            print(item.get_data())

    def calculate_total_cost(self):
        total = 0
        for item in self._items:
            price = item.get_product_price()
            name = item.get_product_name()
            quantity = item.get_product_quantity()
            total += price * quantity
            print(
                f'{name}: {price * quantity} PLN - Ilość sztuk: {quantity}, cena jednostkowa: {price} PLN')
            print(f'Całkowity koszt: {total} PLN')


list1 = List([])
value = input('[d]odaj, [u]suń, [l]istuj, [p]olicz, [z]akończ: ')
while value != 'z':
    if value == 'd':
        name_product = input('Nazwa produktu: ')
        price_product = float(input('Cena produktu: '))
        while price_product <= 0:
            print('Cena produktu musi być większa niż 0')
            price_product = float(input('Cena produktu: '))
        quantity_product = float(input('Ilość produktu: '))
        while quantity_product <= 0:
            print('Ilość produktu musi być większa niż 0')
            quantity_product = float(input('Ilość produktu: '))
        item_product = Product(name_product.capitalize(), price_product)
        list1.add_item(item_product, quantity_product)
    elif value == 'u':
        product_to_remove = input('Podaj nazwę produktu do usunięcia: ')
        product_quantity_to_remove = float(input('Podaj ilość sztuk do usunięcia: '))
        while product_quantity_to_remove <= 0:
            print('Ilość produktu do usunięcia musi być większa niż 0')
            product_quantity_to_remove = float(input('Podaj ilość sztuk do usunięcia: '))
        list1.remove_item(product_to_remove.capitalize(), product_quantity_to_remove)
    elif value == 'l':
        list1.list_items()
    elif value == 'p':
        list1.calculate_total_cost()
    elif value == 'z':
        break
    else:
        print("Błędny wybór!")
    value = input('[d]odaj, [u]suń, [l]istuj, [p]olicz, [z]akończ: ')