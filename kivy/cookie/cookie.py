from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget

class Cookie(FloatLayout): # Cookie dziedziczy po Widget/FloatLayout co tam jest wszystko i do tego może być rozbudowywane o nowe funkcjonalności
    pass

class CookieApp(App): # biblioteka kivy spodzieqwa się pliku cookie bez App w którym szuka...

    def build(self):
        return Cookie() #zamieniłem Widget na Cookie czyli klase bazową dla aplikacji
            #Widget()  # Widget jest to klasa bazowa dla wszystkich okienek w aplikacji
    # Widget to okienko w naaszym przypadku jest to okno główne RODZIC
    # aplikacja może zawirać inne okienka wewnątrz siebie DZIECI przy czym każde okienko ma tylko jednego RODZICA
    # okienka mogą mieć kolejne dzieci

if __name__ == '__main__':
    CookieApp().run()

