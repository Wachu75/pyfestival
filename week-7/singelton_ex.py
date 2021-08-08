class Singleton:
    _INSTANCE = None

# wzorce projektowe ....
#
    @staticmethod           # metoda statyczna
    def get_instance():     # nie ma self. po tym też poznajemy metody statyczne
        if Singleton._INSTANCE is None:         # jeżeli jest None
            Singleton._INSTANCE = Singleton()   # utwórz instancję klasy Singleton

        return Singleton._INSTANCE
# skutek jest taki że za pierwszym razem stworzy instancję Singelton
# za każdym razem zwracany jest ten sam obiekt
# np. połączenie z bazą danych raz łączymy się z bazą danych i przekazujemy ten sam obiekt

app = Singleton.get_instance()

print(app)