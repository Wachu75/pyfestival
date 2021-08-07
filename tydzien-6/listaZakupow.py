'''
przygotuj program który będzie przechowywał listę zakupów. Każdy wpis jest osobnym obiektem klasy ListItem jeśli dany
produkt znajduje się już na liście nie powinien być dodany drugi raz, zamiast tego powinna być zwiększana jego ilość.
produkty do zakupienia przechowuj w zmiennej prywatnej
obiekty klasy List musi posiadać następujące metody
addItem(product: Product, quantity: float)
removeItem(product: Product, quantity: float)
listItem(): list
calculateTotalCost()
każdy produkt klasy Product posiada cenę oraz nazwę
'''
'''
class Product: name,price metody: get_name get_price
'''

class Product:
    def __init__(self, name: str, price: float):
        self._price = price
        self._name = name

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

class List:
    def __init__(self, prod: Product, quantity:  int):
        self.quantity = quantity
        self.prod = prod

    def get_list_products_name(self):
        return self.prod.get_name()

    def get_list_products_price(self):
        return self.prod.get_price()

    def get_quantity(self):
        return self.quantity




    def returnList(self):
        return self.lista_zakupow

    def removeItem(self):
        pass

    def calculateTotalCost(self):
        pass

class ListShop:
    def __init__(self):
        self.lista_zakupow = []  # tworzę pustą listę reszta w addProducts

    def addProduct(self, prod: Product, quantity):
        if isinstance(prod, Product):               # isinstance(arg, class) sprawdza czy argument arg jest typu classy
            self.lista_zakupow.append(List(prod, quantity))
        else:
            print('blad')


    def showList(self):
        tempList = {}
        for prod in self.lista_zakupow:
            print(f'id: {self.lista_zakupow.index(prod)}'
                  f'  produkt: {prod.get_list_products_name()}')


mleko = Product('Mleko', 2.34)
mleko1 = Product('Mleko', 2.35)
maslo = Product('masło', 4.58)
maslo1 = Product('masło', 4.58)


lista = ListShop()

lista.addProduct(mleko, 3)
lista.addProduct(mleko1, 4)
lista.addProduct(maslo, 2)
lista.addProduct(maslo1, 5)

print(lista)

#info = ShowList(lista)
#show_info = info.getInfo()
#print(show_info)
lista1 = lista.showList()
print(lista1)

# print(mleko.price)
# print(mleko.name)
# print(lista.returnList())
