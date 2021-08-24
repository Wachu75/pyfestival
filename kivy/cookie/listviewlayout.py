from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior


class ListViewLayout(RecycleBoxLayout, LayoutSelectionBehavior):
    # metodę select_with_touch dziedziczymy po LayoutSelectionBehavior która dziedziczy ją jeszcze wcześniej ale dzięki temu
    # dziedziczeniu możemy w naszy ListViewLayout z niej kożystać a konkretnie jest to w pliku selectablelabel.py w metodzie on_touch_down
    pass