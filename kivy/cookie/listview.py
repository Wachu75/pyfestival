from kivy.uix.recycleview import RecycleView
from selectablelabel import SelectableLabel
from listviewlayout import ListViewLayout


class ListView(RecycleView):# RecycleView umożliwia włożenie kilku elementów
    def __init__(self, **kwargs):
        super(ListView, self).__init__(**kwargs)
        #item = []
        # for i in range(0,25):
        #     item.append({'text': str(i)})
        # self.data = item
# przez self.data przekazujemy do selecttablelabel.py pewne property którymi się one uzupełaniają czyli na podstawie
# czyli do konstruktowa w selecttablelabel ( tu nie do konca wiem co miał na myśli )
# inaczej naszego konstruktora linia 7 def __init__(self, **kwargs): przez **kwargs przekazuje się zmienna {'text': str(i)}
# o kluczu text i wartości i
