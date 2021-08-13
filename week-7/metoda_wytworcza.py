'''
https://refactoring.guru/pl/design-patterns/factory-method/python/example
Metoda wytwórcza jest kreacyjnym wzorcem projektowym rozwiązującym problem tworzenia obiektów-produktów bez
określania ich konkretnych klas.
Metoda wytwórcza definiuje metodę która ma służyć tworzeniu obiektów bez bezpośredniego wywoływania konstruktora
(poprzez operator new). Podklasy mogą nadpisać tę metodę w celu zmiany klasy tworzonych obiektów.
Przykłady użycia: Wzorzec Metoda wytwórcza jest często stosowany w kodzie Python. Przydaje się gdy chcesz nadać
swojemu kodowi wysoki poziom elastyczności.

Identyfikacja: Metody wytwórcze można poznać po metodach kreacyjnych tworzących obiekty na podstawie konkretnych
klas, ale zwracających typ abstrakcyjny lub interfejs.
Przykład koncepcyjny
Poniższy przykład ilustruje strukturę wzorca projektowego Metoda wytwórcza ze szczególnym naciskiem na następujące
kwestie:

    Z jakich składa się klas?
    Jakie role pełnią te klasy?
    W jaki sposób są ze sobą powiązane elementy wzorca?

'''


from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    Klasa Creator deklaruje metodę fabryczną, która ma zwrócić nam obiekt klasy Product.
    Podklasy Stwórcy zwykle zapewniają:     wdrożenie tej metody.
    """

    @abstractmethod
    def factory_method(self):
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        Pamiętaj, że Creator może również zapewnić domyślną implementację metody fabrycznej.
        """
        pass

    def some_operation(self) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        Zauważ też, że pomimo swojej nazwy, główna odpowiedzialnością Create nie jest tworzenie produktów.
        Zwykle zawiera podstawową logikę biznesową, która opiera się na obiektach Product zwracanych przez metodę fabryczną.
         Podklasy mogą pośrednio zmienić tę logikę biznesową, zastępując
         metodą fabryczną i zwrócająć z niej innego rodzaju produktu.
        """

        # Call the factory method to create a Product object.
        product = self.factory_method()

        # Now, use the product.
        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result


"""
Concrete Creators override the factory method in order to change the resulting
product's type.
Concrete Creators nadpisują metodę fabryczną, aby zmienić wynikowy
rodzaj produktu. 
"""


class ConcreteCreator1(Creator):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
    Zauważ, że podpis metody nadal używa abstrakcyjnego typu produktu,
     nawet jeśli konkretny produkt jest faktycznie zwracany z metody. Ten
     sposób, w jaki Twórca może pozostać niezależny od konkretnych klas produktów.
    """

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    Interfejs produktu deklaruje operacje, które wszystkie konkretne produkty
     musi wdrożyć.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


"""
Concrete Products provide various implementations of the Product interface.
Produkty Concrete zapewniają różne implementacje interfejsu Produktu. 
"""


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


def client_code(creator: Creator) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    Kod klienta działa z instancją konkretnego twórcy, aczkolwiek poprzez
     jego podstawowy interfejs. Dopóki klient nadal współpracuje z twórcą poprzez
     interfejs bazowy, możesz przekazać mu dowolną podklasę twórcy.
    """

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())