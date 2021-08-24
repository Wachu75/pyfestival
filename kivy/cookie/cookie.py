from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from shapebutton import ShapeButton
from picture import Picture
from pictureview import PictureView

class Cookie(FloatLayout): # Cookie dziedziczy po Widget/FloatLayout co tam jest wszystko i do tego może być rozbudowywane o nowe funkcjonalności

    def enable_draw_mode(self, mode):
        self.ids.picture.draw_mode = mode
        self.ids.picture_view.scroll_timeout = 1
        self.ids.picture_view.scroll_distance = 100000

    def disable_draw_mode(self):
        self.ids.picture.draw_mode = ""
        self.ids.picture_view.scroll_timeout = 200
        self.ids.picture_view.scroll_distance = 10

    def shape_button_click(self, button):
        next_state = not button.selected
        self.deactivate_button()
        button.selected = next_state
        print(button.name)
        if next_state:
            self.enable_draw_mode(button.name)

    def deactivate_button(self):
        self.disable_draw_mode()
        for key in self.ids:
            if isinstance(self.ids[key], ShapeButton):
                self.ids[key].selected = False

        # self.ids.line_button.selected = False
        # self.ids.rectangle_button.selected = False
        # self.ids.circle_button.selected = False
        # self.ids.freeform_button.selected = False

    # def line_button_click(self):
    #     next_state = not self.ids.line_button.selected
    #     self.deactivate_button()
    #     self.ids.line_button.selected = next_state
    #     print("line")
    #
    # def rectangle_button_click(self):
    #     next_state = not self.ids.rectangle_button.selected
    #     self.deactivate_button()
    #     self.ids.rectangle_button.selected = next_state
    #     print("rectangle_button_down")
    #
    # def circle_button_click(self):
    #     next_state = not self.ids.circle_button.selected
    #     self.deactivate_button()
    #     self.ids.circle_button.selected = next_state
    #     print("circle_button_down")
    #
    # def freeform_button_click(self):
    #     next_state = not self.ids.freeform_button.selected
    #     self.deactivate_button()
    #     self.ids.freeform_button.selected = next_state
    #     print("freeform_button_down")

class CookieApp(App): # biblioteka kivy spodziewa się pliku cookie bez App w którym szuka...

    def build(self):
        return Cookie() #zamieniłem Widget na Cookie czyli klase bazową dla aplikacji
            #Widget()  # Widget jest to klasa bazowa dla wszystkich okienek w aplikacji
    # Widget to okienko w naaszym przypadku jest to okno główne RODZIC
    # aplikacja może zawirać inne okienka wewnątrz siebie DZIECI przy czym każde okienko ma tylko jednego RODZICA
    # okienka mogą mieć kolejne dzieci

if __name__ == '__main__':
    CookieApp().run()

