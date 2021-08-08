
class A:
    def __init__(self, name, values):
        self._values = values
        self._name = name

    def get_name(self):
        return self._name

    def get_values(self):
        return self._values


class ListElements:
    def __init__(self, name: A, values_list_elements):
        self._values_list_elements = values_list_elements
        self._name = name

    def get_name_a(self):
        return self._name

    def get_values(self):
        return self._values_list_elements

    def get_name_from_class_A(self):
        return self._name.get_name()

    def get_data(self):
        return f'{self._name.get_name()}, {self._name.get_values()}, {self._values_list_elements}'


class BoxListElements:
    def __init__(self, items):
        self._items = items

    def additemstoboxlist(self, name: A, values_list_elements):
        for idx in self._items:
            if idx.get_values_from_class_A == name.get_name():
                current = idx.get_values_from_class_A
        self._items.append(ListElements(name, values_list_elements))


    def list_items(self):
        for item in self._items:
            print(item.get_data())
            print(item.get_values()) # już działa , nie do końca skąd to None na końcu?
            # !!! tu chcę dostać się do atybutu value_list_elements przekazanego przy wywołaniu metody
            # additemstoboxlist(self, name: A, values_list_elements): czyli cyfry 5 ! Jak to zrobić ?
            print(self._items.index(item))

list1 = BoxListElements([])     # tworzona nowa instancja klasy BoxElements zawierająca pusą listę []
a1 = A('a1', 2)                 # tworzona nowa instancja klasy A - od tej pory zmienna a1 posiada pod adresem
                                # <__main__.A object at 0x0000024853FF6C70> w pamięci tą informację
print(a1)

list1.additemstoboxlist(a1, 5)  # na utworzonej instancji wywołujemy metodę z przekazanymi jej argumentami
print(list1)
# co się tu dzieje:
''' list1 jest instancją klasy BoxListElements a metodą w tej klasie jest additemstoboxlist która odbiera jako
argumenty 
1.self - czyli instancję klasy tzn tu przekazany jest list1! 
2.name typu class A -> tu musimy przekazać argument typu class czyli nasze a1 
3.value_list_elements bez konkretnego typu dla nas jest to 5 i właśnie tą wartość chcę odczytać '''

print(list1.list_items())

# uzyskuję =>   a1, 2
#               None
