from kivy.properties import BooleanProperty
from kivy.uix.label import Label
from kivy.uix.recycleview.views import RecycleDataViewBehavior


class SelectableLabel(Label, RecycleDataViewBehavior):
    selected = BooleanProperty(False)
# SelectableLabel będzie dziedziczyła po RecycleDataViewBehavior któa ma metody króre chcemy rozszerzyć refresh_view_attrs
# refresh_view_attrs jest za każdym razem odświerzane gdy w pliku listview.py self.data = item się zmienia !
#
    index = None
# refresh_view_attrs jest z klasy bazowej !
    def refresh_view_attrs(self, rv, index, data): # index jest to nr porzędkowy elementu na liście po prawqej stronie
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(rv, index, data) # zwracam metode klasy bazowej

    def on_touch_down(self, touch): # definiujemy metodę co się zadzieje jak się kliknie w tą tabelkę
        if self.collide_point(touch.x, touch.y):  # jeżeli tabelka coliduje z miejscem w które ktoś kliknął
            self.parent.select_with_touch(self.index, touch) # to chcę wywołać z parent wywołać metode select_with_touch

    def apply_selection(self, rv, index, is_selected): # jest z klasy bazowej!
        self.selected = is_selected